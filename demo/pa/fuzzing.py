'''
Script che emette una serie di payload verso il microcontroller
e salva in tracce separate il risultato.

Il setup consiste in un computer collegato con una sonda
al led e contemporaneamente con la seriale allo sketch.


NOTA
----

Se sei in dubbio che si pianti il computer per troppa memoria
usata, puoi configurare ulimit per poco meno di 5GB di utilizzo
di memoria virtuale.

 $ ulimit -Sv 5000000

In particolare usare una list con append() al posto di extend() altrimenti
goes banana con la memoria.
'''
from PyHT6022.LibUsbScope import Oscilloscope
from threading import Thread
import sys
import string
import time
from struct import pack

from pwnlib.tubes.serialtube import serialtube
from pwn import log as logger

g_data = {}
g_payload = None

sample_rate_index = 30 # 30MS/s
voltage_range = 0x01   # 5V
numchannels = 1
blocksize = 6*1024     # should be divisible by 6*1024


def serial_initialize(port):
    s = serialtube(port, 9600)

    return s

def setup_scope():
    scope = Oscilloscope()
    if not scope.setup():
        raise AttributeError('Scope not available!')
    scope.open_handle()

    if (not scope.is_device_firmware_present):
        logger.info('flash firmware')
        scope.flash_firmware()
    else:
        scope.supports_single_channel = True;

    logger.info("Setting up scope!")

    scope.set_interface(1) # choose ISO
    logger.info('%s %s' % ("ISO" if scope.is_iso else "BULK", "packet size: %d" % scope.packetsize))
    scope.set_num_channels(numchannels)
    scope.set_ch1_voltage_range(voltage_range)
    scope.set_sample_rate(sample_rate_index)

    time.sleep(1)

    return scope

def setup_async_read(s):
    def _data_extend(ch1, ch2):
        if not g_data.has_key(g_payload):
            g_data[g_payload] = []

        g_data[g_payload].append(ch1)

    return s.read_async(
        _data_extend,
        blocksize,
        outstanding_transfers=10,
        raw=True) # w/o raw async doesn't work

def export_to_wav(filepath, samples, samplerate):
    # we divide by 100 because otherwise audacity lets us not zoom into it
    samplerate = samplerate * 1000 * 10
    total = sum(len(block) for block in samples)
    with logger.progress('writing RIFF file %s' % filepath) as progress:
        with open(filepath, "wb") as wf:
            wf.write(b"RIFF")
            wf.write(pack("<L", 44 + total - 8))
            wf.write(b"WAVE")
            wf.write(b"fmt \x10\x00\x00\x00\x01\x00\x01\x00") # http://soundfile.sapp.org/doc/WaveFormat/
            wf.write(pack("<L", samplerate)) # samplerate
            wf.write(pack("<L", samplerate)) # ByteRate
            wf.write(b"\x01\x00\x08\x00")
            wf.write(b"data")
            wf.write(pack("<L", total))
            for block in samples:
                wf.write(block)

g_running = True

def scope_thread_polling(scope):
    # la sonda la facciamo pollare in un thread a parte
    # altrimenti non arrivano i dati
    while g_running:
        scope.poll()


if __name__ == '__main__':
    scope = setup_scope()
    port = sys.argv[1]
    serial = serial_initialize(port)

    shutdown_event = setup_async_read(scope)

    scope.start_capture()
    start_time = time.time()

    payloads = [
        #'\x00'*6,
        #'b',
        #'ca',
        '123456',
        'mazinga',
        'Mazinga',
        'antani',
    ]


    logger.info('starting scope polling thread')

    thread = Thread(target=scope_thread_polling, args=(scope,))
    thread.start()

    with logger.progress('capturing data') as progress:
        for payload in payloads:
            g_payload = payload

            elapsed = time.time() - start_time

            serial.write(payload)
            logger.info('serial output: %s' %  repr(serial.read(timeout=2)))

            time.sleep(1.5)

            progress.status('[%s] elapsed %d seconds' % (payload, elapsed, ))
        else:
            g_running = False
            thread.join()

    logger.info("Stopping new transfers.")
    shutdown_event.set()
    time.sleep(1)
    logger.info("Closing handle")
    scope.stop_capture()
    scope.close_handle()

    logger.info('# data blocks: %d' % len(g_data))

    for payload in g_data.keys():
        export_to_wav('/tmp/scope.%s.wav' % payload, g_data[payload], sample_rate_index)
