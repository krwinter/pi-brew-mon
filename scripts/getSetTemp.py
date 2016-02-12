#! /usr/bin/env python

import sys
import os

# print 'os=' + os.name

# import platform
# print 'platform=' + platform.system() + ' release=' + platform.release()

from config import vars as config
# print "myvar=" + config.MY_VAR 

target_temp_file = os.path.join(os.path.dirname(sys.argv[0])) + '/config/target_temp.txt'

def get_set_temp():
    # for now just a number in a file
    f = open(target_temp_file, 'r')
    read_temp = f.readlines()
    f.close()

    # convert
    read_temp = int(read_temp[0])

    return read_temp

#TODO - set so can use as cmd line or part of main daemon
print str(get_set_temp()) + config.MY_VAR
#print 999999