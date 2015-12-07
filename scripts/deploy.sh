#deploy to pi

scp -r -i /Users/kwinter/.ssh/id_rsa_pi /Users/kwinter/Documents/workspaces/pi/pi-brew-mon/web ken@pi:/home/ken/brewPi/pi-brew-mon
scp -i /Users/kwinter/.ssh/id_rsa_pi -r /Users/kwinter/Documents/workspaces/pi/pi-brew-mon/scripts ken@pi:/home/ken/brewPi/pi-brew-mon
scp -i /Users/kwinter/.ssh/id_rsa_pi -r /Users/kwinter/Documents/workspaces/pi/node-restify-api-gateway/app ken@pi:/home/ken/brewPi/node-pi