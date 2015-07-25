#temp controller# temp controller
import os
import glob
import time


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


device_dir = '/sys/bus/w1/devices/'
data_dir = '/home/ken/pi-brew-mon/scripts/data/' # not yet used

datafile_name = 'data/datafile' + str(time.strftime( "%Y%m%d_%H%M%S", time.localtime())) + '.csv'
print "Creating datafile" + datafile_name

def setup():
    os.system('gpio -g mode 17 out')
    os.system('gpio -g mode 22 out')

    with open(datafile_name, 'a') as datafile:
            header = 'timestamp,t1,t2,t3,relay_state' + '\n'
            datafile.write(header)


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

    return all_temps



def generate_row(temps,relay_state):
    #import ipdb;ipdb.set_trace()
    rowvals = (str(int(time.time())),str(temps[0]),str(temps[1]),str(temps[2]),str(relay_state))
    row = ','.join(rowvals)
    return row

def get_relay_state():
    global set_relay_state
    measured_relay_state = os.system('gpio -g read 17')
    if measured_relay_state != set_relay_state:
        set_relay_state = measured_relay_state
        print "*** Changing relay to {0} ***".format(relay_state)
    return measured_relay_state;

def check_if_switch_relays(temp):
    if temp >= target_temp + upper_limit:
            relay_off()

    if temp <= target_temp - lower_limit:
            relay_on()


def relay_on():
    print "** Turning relay on **"
    os.system('gpio -g write 17 1')


def relay_off():
    print "** Turning relay off **"
    os.system('gpio -g write 17 0')


def main():

    setup()

    print "Looping...."

    while True:
        with open(datafile_name, 'a') as datafile:

            temps = get_temps()

            check_if_switch_relays(temps[1])

            relay_state = get_relay_state()

            row = generate_row(temps, relay_state)

            datafile.write(row + '\n')

        time.sleep(5)


main()