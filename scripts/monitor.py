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


target_temp = 20
upper_limit = 1
lower_limit = 1

#base_dir = '/sys/bus/w1/devices/'
base_dir = '/Users/kwinter/Documents/workspaces/pi/data/'

logfile_name = 'logfile' + str(strftime( "%Y%m%d%H%M%S", time.time()) + '.csv'
print "Creating logfile" + logfile_name

def setup():
    os.system('gpio -g mode 17 out')
    os.system('gpio -g mode 22 out')

    with open(logfile_name, 'a') as logfile:
            header = 'timestamp,t1,t2,t3,relay_state' + '\n'
            logfile.write(header)

# def read_temp_raw(device_file):
#     f = open(device_file, 'r')
#     lines = f.readlines()
#     f.close()
#     return lines

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
        return temp_f



def get_temps():

    all_temps = []

    for f in range(3):
        # we should have 3 - which is which???
        device_folder = glob.glob(base_dir + '28*')[f]
        device_file = device_folder + '/w1_slave'

        all_temps.append(read_temp(device_file))

    return all_temps



def generate_row(temps,relay_state):
    #import ipdb;ipdb.set_trace()
    rowvals = (str(int(time.time())),str(temps[0]),str(temps[1]),str(temps[2]),str(relay_state))
    row = ','.join(rowvals)
    return row

def get_relay_state():
    return 1;

def check_if_switch_relays(temp):
    if temp >= target_temp + upper_limit:
            relay_off()

    if temp <= target_temp - lower_limit:
            relay_on()


def relay_on():
    os.system('gpio -g write 17 1')


def relay_off():
    os.system('gpio -g write 17 0')


def main():

    setup()

    while True:
        print "Looping...."
        with open(logfile_name, 'a') as logfile:

            temps = get_temps()

            check_if_switch_relays(temps[0])

            relay_state = get_relay_state()

            row = generate_row(temps, relay_state)

            logfile.write(row + '\n')

        time.sleep(5)


main()