import sys
import os

#target_temp_file = 'app/python/config/target_temp.txt'
target_temp_file = os.path.join(os.path.dirname(sys.argv[0])) + '/config/target_temp.txt'

def get_set_temp():
    # for now just a number in a file
    f = open(target_temp_file, 'r')
    read_temp = f.readlines()
    f.close()

    # convert
    read_temp = int(read_temp[0])

    return read_temp

print get_set_temp()