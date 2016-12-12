#deploy to pi
rsync -avx -e 'ssh -i /Users/kwinter/.ssh/id_rsa' --progress /Users/kwinter/Documents/workspaces/pi/node-restify-api-gateway/app ken@brewtemp-pi:/home/ken/brewPi/node-pi
rsync -avx -e 'ssh -i /Users/kwinter/.ssh/id_rsa' --progress /Users/kwinter/Documents/workspaces/pi/node-restify-api-gateway/config ken@brewtemp-pi:/home/ken/brewPi/node-pi
rsync -avx -e 'ssh -i /Users/kwinter/.ssh/id_rsa' --progress /Users/kwinter/Documents/workspaces/pi/node-restify-api-gateway/fermnode ken@brewtemp-pi:/home/ken/brewPi/node-pi
rsync -avx -e 'ssh -i /Users/kwinter/.ssh/id_rsa' --exclude '/data' /Users/kwinter/Documents/workspaces/pi/pi-brew-mon/scripts ken@brewtemp-pi:/home/ken/brewPi/pi-brew-mon
rsync -avx -e 'ssh -i /Users/kwinter/.ssh/id_rsa' /Users/kwinter/Documents/workspaces/pi/react-brew-dash/dist ken@brewtemp-pi:/home/ken/brewPi/react-brew-dash


