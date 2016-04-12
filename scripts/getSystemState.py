#! /usr/bin/env python


from subprocess import call, check_output
import psutil

# make sure monitor process is running
# OPTIONAL - check GPIO is init and set correctly

def get_system_state():

	#call(["ls", "-l"])
	#running = check_output(["ps aux | grep python | grep monitor.py"], shell=True)

	running = 0

	for proc in psutil.process_iter():
	    try:
	        pinfo = proc.as_dict(attrs=['pid', 'name', 'exe', 'cmdline'])
	    except psutil.NoSuchProcess:
	        pass
	    else:
	    	#processCommand = pinfo['cmdline']
			#print (pinfo['cmdline'])
			shell_command = pinfo['cmdline']
			#print shell_command
			if shell_command and 'python' in shell_command[0] and len(shell_command) > 0 and 'run.py' in shell_command[1]:
				running = 1
				break
				os.system('kill %d' % os.getpid())


	return running


if __name__ == "__main__":
	print get_system_state()
	