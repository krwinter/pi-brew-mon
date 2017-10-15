#! /usr/bin/env python

import sys
import os

from config import vars as config

device_dir = config.READ_TEMP_DIR

def read_temp_raw(device_file):
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp(device_file):
    #ipdb.set_trace()
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
    device_file = device_dir + '/w1_slave'
    current_temp = read_temp(device_file)
    return current_temp


if __name__ == "__main__":
    print str(get_current_temp())
