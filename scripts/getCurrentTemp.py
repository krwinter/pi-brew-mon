#! /usr/bin/env python

import sys
import os
import glob

from config import vars as config

device_dir = config.READ_TEMP_DIR

def read_temp_raw(device_file):
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp(device_file):
    lines = read_temp_raw(device_file)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = round(float(temp_string) / 1000.0, 2)
        temp_f = round(temp_c * 9.0 / 5.0 + 32.0, 2)
        return temp_c

def get_current_temp():

    if config.ENV == 'pi':
        total_temp_sensors = 1
    else:
        total_temp_sensors = 1

    all_temps = []
    for f in range(total_temp_sensors):
        # we should have 3 - which is which???
        #print 'device dir is ' + os.path.abspath(device_dir) + ' and glob is ' + "+".join(glob.glob(device_dir + '28*'))
        #device_folder = glob.glob(device_dir + '28*')[f]
        device_folder = '/sys/devices/w1_bus_master1/28-00000520ce11'
        device_file = device_folder + '/w1_slave'

        temp = read_temp(device_file)

        #print "Temp for {0} is {1}".format(device_file, temp)

        all_temps.append(temp)

    #print "---"
    # just the 1st one for now
    return all_temps[0]

if __name__ == "__main__":
    print get_current_temp()


