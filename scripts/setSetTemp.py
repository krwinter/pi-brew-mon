#! /usr/bin/env python

import sys
import os

# print 'os=' + os.name

# import platform
# print 'platform=' + platform.system() + ' release=' + platform.release()

from config import vars as config
# print "myvar=" + config.MY_VAR 

target_temp_file = os.path.join(os.path.dirname(sys.argv[0])) + '/config/target_temp.txt'

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass


# TODO - replace this with a call to the getSetTemp.py
def get_set_temp():
    # for now just a number in a file
    f = open(target_temp_file, 'r')
    read_temp = f.readlines()
    f.close()

    if is_number(read_temp[0]):
        # convert
        read_temp = float(read_temp[0])
    else:
        read_temp = "NaN"

    return read_temp


def set_set_temp(temp):
    # for now just a number in a file
    print temp
    if is_number(temp) and float(temp) >= config.MIN_SET_TEMP and float(temp) <= config.MAX_SET_TEMP: 
        f = open(target_temp_file, 'w')
        f.write(temp)
        f.close()
        return True
    else:
        return False


#TODO - set so can use as cmd line or part of main daemon
set_set_temp(sys.argv[1])
print str(get_set_temp())
#print 999999