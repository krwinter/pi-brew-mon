#!/bin/bash

sudo modprobe w1-gpio
sudo modprobe w1-therm

gpio -g mode 17 out
gpio -g mode 22 out

echo "Initializing temperature controller"
#echo "Format:"
#echo "gpio -g write 22 0"
#echo "17 and 22 are the relays, 0 and 1 are on and off"

# now get python env set up
workon pi-mon
./monitor.py

#/home/ken/.virtualenvs/pi-mon/bin/python monitor.py