# https://pythonhosted.org/RPIO/rpio_py.html
from PyHT6022.LibUsbScope import Oscilloscope
#import pylab
import time
import sys
import string
import time

from pwnlib.tubes.serialtube import serialtube


if __name__ == '__main__':
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


def apply_data_smoothing(data, window=1):
    new_data = data[:window]
    for i, point in enumerate(data[window:-window]):
        new_data.append(sum(data[i-window:i+window+1])/(2*window+1))
    new_data.extend(data[-window:])
    return new_data

def setup_scope():
    sample_rate_index = 0x04
    voltage_range = 0x01
    data_points = 0x2000

    scope = Oscilloscope()
    scope.setup()
    scope.open_handle()

    if (not scope.is_device_firmware_present):
        scope.flash_firmware()
    else:
        scope.supports_single_channel = True;
    print("Setting up scope!")
    scope.set_sample_rate(sample_rate_index)
    scope.set_ch1_voltage_range(voltage_range)

    ch1_data, _ = scope.read_data(data_points)#,raw=True)#timeout=1)

    voltage_data = scope.scale_read_data(ch1_data, voltage_range)
    timing_data, _ = scope.convert_sampling_rate_to_measurement_times(data_points, sample_rate_index)
    scope.close_handle()

    if len(timing_data) != len(voltage_data):
        w = sys.stderr.write
        w('data lengths differ!\n')
        w(str([(s,len(eval(s+'_data')))for s in 'timing voltage'.split()]))
        w('\n')
        exit(1)

    # store the data
    with open('/tmp/scopevis.dat', 'wt') as ouf:
        ouf.write('\n'.join('{:8f}'.format(v) for v in voltage_data))
        ouf.write('\n')

    pylab.title('Scope Visualization Example')
    pylab.plot(timing_data, voltage_data, color='#009900', label='Raw Trace')
    pylab.xlabel('Time (s)')
    pylab.ylabel('Voltage (V)')
    pylab.grid()
    pylab.legend(loc='best')
    pylab.xticks(rotation=30)
    pylab.tight_layout()
    pylab.show()
