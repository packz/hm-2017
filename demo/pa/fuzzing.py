'''
Script che emette una serie di payload verso il microcontroller
e salva in tracce separate il risultato.

Il setup consiste nella sonda con GND a valle di una resistenza;
il collegamento con la seriale deve passare attraverso
un ponte wireless per evitare un ground loop.

478000 - 730000 = 250000

240000 - 480000 = 240000

310000 - 550000 ~ 240000

73000 - 315000 ~ 240000

Come noise misuro 8 mV di picco (senza microcontroller alimentato)
Come noise misuro 100mv di picco (con uC alimentato) frequenza di 1.8MHz + 500kHz

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
import matplotlib.pyplot as plt
from threading import Thread
import itertools
import sys
import string
import time
from struct import pack

from pwnlib.tubes.serialtube import serialtube
from pwn import log as logger

g_data = {}
g_payload = None
N_SAMPLES = 20000000

# questo lo uso per avere un oggetto
# in cui metterci il noise
class NOISE:
    pass

sample_rate_index = 30 # 30MS/s
voltage_range = 0x05   # 500mV
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
    with logger.progress('writing RIFF file %s with sample rate of %d' % (filepath, samplerate)) as progress:
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


def noise(t):
    global g_payload

    g_payload = NOISE

    running = True
    start_time = time.time()
    with logger.progress('capturing data for noise') as progress:
        while running:
            elapsed = time.time() - start_time
            progress.status('elapsed %d of %d seconds' % (elapsed, t))
            running = elapsed < t

    g_payload = None

if __name__ == '__main__':
    scope = setup_scope()
    port = sys.argv[1]
    serial = serial_initialize(port)

    shutdown_event = setup_async_read(scope)

    scope.start_capture()

    logger.info('starting scope polling thread')

    thread = Thread(target=scope_thread_polling, args=(scope,))
    thread.start()

    #noise(5)

    start_time = time.time()

    payloads = [
        #'\x00'*6,
        #'b',
        #'ca',
        '123456',
        'mazing',
        'Mazing',
        #'antani',
    ]

    with logger.progress('capturing data') as progress:
        for payload in payloads:
            for index in xrange(10):
                g_payload = '%s.%d'  % (payload, index)

                serial.write(payload)
                logger.info('serial output: %s' %  repr(serial.read(timeout=2)))

                time.sleep(.5)

                elapsed = time.time() - start_time
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

    sys.exit(0)

    plt.ion()

    for index in xrange(2):
        d = list(itertools.chain.from_iterable(g_data['123456.%d' % index]))[:N_SAMPLES]
        timing_data, _ = scope.convert_sampling_rate_to_measurement_times(len(d), sample_rate_index)
        plt.plot(timing_data, d)

    while True:
        plt.pause(0.5)
