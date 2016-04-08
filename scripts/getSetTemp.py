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
    read_temp = float(read_temp[0])

    return read_temp

if __name__ == "__main__":
	print str(get_set_temp())
