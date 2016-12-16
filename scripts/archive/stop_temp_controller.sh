#!/bin/bash

sudo modprobe w1-gpio
sudo modprobe w1-therm

gpio -g mode 17 out
gpio -g mode 22 out

gpio -g write 17 0
gpio -g write 22 0

echo "Turning OFF all relays:"
#echo "gpio -g write 17 0"
#echo "gpio -g write 22 0"
#echo "17 and 22 are the relays, 0 and 1 are on and off"