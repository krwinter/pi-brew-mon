#temp controller
import os
import glob
import time

import RPi.GPIO as GPIO


# --- set up / init - modprobe, gpio settings, etc

# --- main loop

# do every x seconds (60)
# check temp of both probes
# check against target range - when on, when off
# change heater status if necessary
# check heater status
# write to file


target_temp = 22
upper_limit = 1
lower_limit = 1

set_relay_state = 0
set_target_temp = 0

gpio_pin = 17


device_dir = '/sys/bus/w1/devices/'
data_dir = '/home/ken/pi-brew-mon/scripts/data/'  #TODO - make relative
target_temp_file = '/home/ken/pi-brew-mon/scripts/config/target_temp.txt'

datafile_name = 'data/datafile' + str(time.strftime( "%Y%m%d_%H%M%S", time.localtime())) + '.csv'
print "Creating datafile" + datafile_name

def setup():
    #os.system('gpio -g mode 17 out')
    #os.system('gpio -g mode 22 out')

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gpio_pin, GPIO.OUT)

    with open(datafile_name, 'a') as datafile:
            header = 'timestamp,set_temp,t1,t2,t3,relay_state' + '\n'
            datafile.write(header)


def get_set_temp():
    # for now just a number in a file
    f = open(target_temp_file, 'r')
    read_temp = f.readlines()
    f.close()

    # convert
    read_temp = int(read_temp[0])

    global set_target_temp
    if set_target_temp != read_temp:
        print "-! Target Temp changed to {0}".format(read_temp)

    set_target_temp = read_temp

    return read_temp


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

        print "Temp for {0} is {1}".format(device_file, temp)

        all_temps.append(temp)

    print "---"
    return all_temps



def generate_row(set_temp,temps,relay_state):
    #import ipdb;ipdb.set_trace()
    rowvals = (str(int(time.time())),str(set_temp),str(temps[0]),str(temps[1]),str(temps[2]),str(relay_state))
    row = ','.join(rowvals)
    return row

def get_relay_state():
    #return os.system('gpio -g read 17');
    return GPIO.input(gpio_pin)


def check_if_switch_relay(set_temp, read_temp):
    desired_relay_state = 0

    if read_temp >= set_temp + upper_limit:
        desired_relay_state = 0

    if read_temp <= set_temp - lower_limit:
        desired_relay_state = 1

    global set_relay_state
    if set_relay_state != desired_relay_state:
        set_relay_state = desired_relay_state
        set_relay(set_relay_state)
        print "*** Change relay to {0} ***".format(set_relay_state)


def set_relay(relay_state):
    GPIO.output(gpio_pin, relay_state)
    print " --SET RELAY-- Setting GPIO to state {0}".format(relay_state)

    #cmd = 'gpio -g write 17 ' + str(relay_state)
    #print "--running command: " + cmd
    #os.system(cmd)



def main():

    setup()

    print "Looping...."

    while True:
        with open(datafile_name, 'a') as datafile:

            read_temps = get_temps()

            set_temp = get_set_temp()

            check_if_switch_relay(set_temp, read_temps[1])

            relay_state = get_relay_state()

            row = generate_row(set_temp, read_temps, relay_state)

            datafile.write(row + '\n')

        time.sleep(5)


main()