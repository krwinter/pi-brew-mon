#! /usr/bin/env python

import sys
import os
from updateHardwareSettings import updateHardwareSettings



from config import vars as config
from getSetTemp import get_set_temp

target_temp_file = os.path.join(os.path.dirname(sys.argv[0])) + '/config/target_temp.txt'

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass


def set_set_temp(temp):
    # for now just a number in a file
    if is_number(temp) and float(temp) >= config.MIN_SET_TEMP and float(temp) <= config.MAX_SET_TEMP:
        f = open(target_temp_file, 'w')
        f.write(temp)
        f.close()

        # since temp changed, force hardware update (independent of service that may be running)
        updateHardwareSettings();

        return True
    else:
        return False


#TODO - set so can use as cmd line or part of main daemon
if __name__ == "__main__":
    set_set_temp(sys.argv[1])
    print str(get_set_temp())
#print 999999
