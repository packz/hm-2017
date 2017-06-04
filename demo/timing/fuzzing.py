'''
Se sei in dubbio che si pianti il computer per troppa memoria
usata, puoi configurare ulimit per poco meno di 5GB di utilizzo
di memoria virtuale.

 $ ulimit -Sv 5000000

Usare una list con append() al posto di extend() altrimenti
goes banana con la memoria.
'''
# https://pythonhosted.org/RPIO/rpio_py.html
#import matplotlib
#matplotlib.use('wxAgg')

from PyHT6022.LibUsbScope import Oscilloscope
#import pylab
import sys
import string
import time
from struct import pack
from collections import deque

from pwnlib.tubes.serialtube import serialtube
from pwn import log as logger

data = []

sample_rate_index = 30 # 48MS/s
voltage_range = 0x01     # 5V
numchannels = 1
blocksize = 6*1024      # should be divisible by 6*1024


def usage(progname):
    print >> sys.stderr, "usage: %s [--no-serial | --no-scope]" % progname
    sys.exit(1)

def serial_stuffs():
    s = serialtube('/dev/ttyUSB0', 9600)

    words = [ # first, all 1s
        '\x7F',
        '\x7F\x7F',
        '\x7F\x7F\x7f',
        '~', # then, we want one bit flipped
        '~~',
        '~~~',
    ] + list(string.lowercase)

    for word in words:
        s.write(word)

        print s.read()

        time.sleep(1.0)

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
    return s.read_async(
        lambda ch1_data, ch2_data: data.append(ch1_data),
        blocksize,
        outstanding_transfers=10,
        raw=True) # w/o raw async doesn't work

def export_to_wav(filepath, total, samplerate):
    # we divide by 100 because otherwise audacity lets us not zoom into it
    samplerate = samplerate * 1000 * 10
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
            for block in data:
                wf.write(block)

def humanize_data(s):
    #timing_data, _ = s.convert_sampling_rate_to_measurement_times(len(data), sample_rate_index)

    filepath = '/tmp/scopevis.dat'
    with logger.progress('saving data into %s' % filepath) as progress:
        with open(filepath, 'wb') as ouf:
            size = len(data)
            for index in xrange(size):
                if index % 1000 == 0:
                    progress.status('writing block %d of %d' % (index, size))

                d = data[index]
                #voltage_data = s.scale_read_data(d, voltage_range)
                ouf.write(d)

    logger.info('plotting like a boss')
    #from bokeh.plotting import figure, output_file, show

    #output_file("line.html")

    #p = figure(plot_width=400, plot_height=400)

    # add a line renderer
    #p.line(timing_data, voltage_data, line_width=2)

    #show(p)

    import iteritools

    pylab.title('Scope Visualization Example')
    pylab.plot(iteritools.chain.from_iterables(data), color='#009900', label='Raw Trace')
    pylab.xlabel('Time (s)')
    pylab.ylabel('Voltage (V)')
    pylab.grid()
    pylab.legend(loc='best')
    pylab.xticks(rotation=30)
    pylab.tight_layout()
    pylab.show()

def check():
    import itertools
    print set(itertools.chain.from_iterable(data))


if __name__ == '__main__':
    n_seconds = int(sys.argv[1])
    scope = setup_scope()

    shutdown_event = setup_async_read(scope)

    scope.start_capture()
    start_time = time.time()
    running = True
    with logger.progress('capturing data') as progress:
        while running:
            scope.poll()
            elapsed = time.time() - start_time
            running = elapsed < n_seconds
            progress.status('elapsed %d of %d seconds' % (elapsed, n_seconds))

    logger.info("Stopping new transfers.")
    shutdown_event.set()
    time.sleep(1)
    logger.info("Closing handle")
    scope.stop_capture()
    scope.close_handle()

    logger.info('# data blocks: %d' % len(data))
    #humanize_data(scope)
    #check()
    total = sum(len(block) for block in data)
    logger.info('total: %d' % total)
    export_to_wav('/tmp/scope.wav', total, sample_rate_index)
