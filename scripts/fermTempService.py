#!/home/ken/.virtualenvs/brewtemp/bin/python

#temp controller
import os
import sys
import glob
import time
import logging

from config import vars as config

from getSetTemp import get_set_temp
from getRelayMode import get_relay_mode
from getRelayState import get_relay_state
from getCurrentTemp import get_current_temp
from setRelayState import set_relay_state
from setSystemState import set_system_state
#import ipdb;ipdb.set_trace()

base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
#base_dir = os.path.join(os.path.dirname(sys.argv[0]))
config_dir = base_dir   + '/config/'
data_dir = base_dir   + '/data/'
set_temp_file = config_dir + 'target_temp.txt'
poll_interval_file = config_dir + 'poll_interval.txt'
log_interval_file = config_dir + 'log_interval.txt'

# datafile_name = 'data/datafile' + str(time.strftime( "%Y%m%d_%H%M%S", time.localtime())) + '.csv'
# print "Creating datafile" + datafile_name

device_dir = '/sys/bus/w1/devices/'

logfilename='/var/log/fermtemp.log'

# how much we need to be away from set temp to take action
upper_temp_slop = 0.5
lower_temp_slop = 0.5

#logging
#logging.basicConfig(filename=logfilename,level=logging.INFO, format='%(asctime)s %(message)s')


# RUN

'''
- make sure gpio is set up properly
- make sure we're using the right python env

START:
0. read polling interval / data record interval - loop accordingly
do while:
1. read relayMode - on, off, auto
    if on/off, make sure set
    else is auto
2. read set temp
3. relay on or off
4. record data if needed

'''

def startup():

    #set_system_state(1) # already done by service - we're running here aren't we
    setup_gpio()

    #get_polling_config()


def setup_gpio():
    if config.ENV == 'pi' or os.path.isdir('/sys/bus/w1/devices/'):
        import RPi.GPIO as GPIO
        os.system('sudo modprobe w1-gpio')
        os.system('sudo modprobe w1-therm')
        os.system('gpio -g mode 17 out')
        os.system('gpio -g mode 22 out')

        gpio_pin = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(gpio_pin, GPIO.OUT)
    log_info("GPIO hardware turned ON")


def get_polling_config():

    # for now just a string in a file
    f = open(poll_interval_file, 'r')
    poll_interval = f.readlines()[0]
    f.close()

    f = open(log_interval_file, 'r')
    log_interval = f.readlines()[0]
    f.close()

    log_info("Polling interval is {0} seconds".format(poll_interval))
    log_info("Logging interval is {0} seconds".format(log_interval))

    return int(poll_interval), int(log_interval)


def create_logfile():
    with open(datafile_name, 'a') as datafile:
        header = 'timestamp,set_temp,t1,t2,t3,relay_state' + '\n'
        datafile.write(header)


def set_relay_state_based_on_mode(relay_mode):

    if relay_mode == 'on':
        set_relay_state(1)
    elif relay_mode == 'off':
        set_relay_state(0)


# in this instance we're heating
def set_relay_state_based_on_temps():
    set_temp = get_set_temp()
    current_temp = get_current_temp()
    log_data("setTemp: {0}, currentTemp: {1}".format(set_temp, current_temp))
    desired_relay_state = 0

    if current_temp >= set_temp + upper_temp_slop:
        desired_relay_state = 0

    if current_temp <= set_temp - lower_temp_slop:
        desired_relay_state = 1

    relay_state = get_relay_state()
    if relay_state != desired_relay_state:
        relay_state = desired_relay_state
        set_relay_state(relay_state)
        log_info("*** Change relay to {0} ***".format(relay_state))


def generate_row(set_temp,temps,relay_state):
    with open(datafile_name, 'a') as datafile:
        row = generate_row(set_temp, read_temps, relay_state)
        datafile.write(row + '\n')
        datafile.close()

    #import ipdb;ipdb.set_trace()
    rowvals = (str(int(time.time())),str(set_temp),str(temps[0]),str(temps[1]),str(temps[2]),str(relay_state))
    row = ','.join(rowvals)
    return row

def log_info(message):
    # just print for now
    print message

def log_data(data):
    # just print for now
    log_info("*** " + data)

    #post to log server


def main():

    startup()

    poll_interval, log_interval = get_polling_config()

    log_info("STARTING MAIN EVENT LOOP");

    loop_counter = 1
    while True:

        mode = get_relay_mode() # current temp, set temp, relay mode

        if mode == 'on' or mode == 'off':
            set_relay_state_based_on_mode(mode)
        elif mode == 'auto':
            set_relay_state_based_on_temps()
        # else shutdown???

        if log_interval%poll_interval == 0:
            #write_data()
            pass

        # # get and write the real temp from device (which is blocking) every 4 polls
        # # TODO - use a separate thread?
        # if loop_counter%4 == 0:
        #     print "Now we copy current temp from device"
        #     cache_current_temp();
        #     loop_counter = 1
        # else:
        #     loop_counter+=1

        time.sleep(int(poll_interval))


main()
