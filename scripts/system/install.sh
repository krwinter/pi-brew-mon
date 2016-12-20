#!/bin/bash

sudo cp /opt/fermtemp/system/fermtemp-svc /etc/init.d/fermtemp
sudo cp /opt/fermnode/fermnode-svc /etc/init.d/fermnode
sudo chmod +x /etc/init.d/ferm*
