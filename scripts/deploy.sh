#deploy to pi
rsync -avx -e 'ssh -i /Users/kwinter/.ssh/id_rsa_pi' --progress /Users/kwinter/Documents/workspaces/pi/node-restify-api-gateway/app ken@pi:/home/ken/brewPi/node-pi
rsync -avx -e 'ssh -i /Users/kwinter/.ssh/id_rsa_pi' --progress /Users/kwinter/Documents/workspaces/pi/node-restify-api-gateway/config ken@pi:/home/ken/brewPi/node-pi
rsync -avx -e 'ssh -i /Users/kwinter/.ssh/id_rsa_pi' --exclude '/data' /Users/kwinter/Documents/workspaces/pi/pi-brew-mon/scripts ken@pi:/home/ken/brewPi/pi-brew-mon


