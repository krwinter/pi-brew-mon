#! /usr/bin/env python

import sys
import os
import glob
import ipdb

from config import vars as config
from getCurrentTemp import get_current_temp


def write_current_temp(temp):
    #ipdb.set_trace()
    f = open(config.CURRENT_TEMP_CACHE, 'w')
    f.write(str(temp))
    f.close()

# the function invoked from outside
def cache_current_temp():
    current_temp = get_current_temp()
    written_temp = write_current_temp(current_temp)
    return written_temp

if __name__ == "__main__":
    cache_current_temp()
    print current_temp
