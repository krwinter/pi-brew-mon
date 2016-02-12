#! /usr/bin/env python

import sys
import os
import glob


device_dir = '/sys/bus/w1/devices/'

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

def get_temps():

    all_temps = []
    for f in range(3):
        # we should have 3 - which is which???
        device_folder = glob.glob(device_dir + '28*')[f]
        device_file = device_folder + '/w1_slave'

        temp = read_temp(device_file)

        #print "Temp for {0} is {1}".format(device_file, temp)

        all_temps.append(temp)

    #print "---"
    return all_temps

#TODO - set so can use as cmd line or part of main daemon
print get_temps()