#! /usr/bin/env python
#import ipdb
#import psutil

from subprocess import call, check_output

# make sure monitor process is running
# OPTIONAL - check GPIO is init and set correctly

#@profile
def get_system_state():

	#TODO - call service status command

	running = 0

	# for proc in psutil.process_iter():
	#     try:
	#         pinfo = proc.as_dict(attrs=['pid', 'name', 'exe', 'cmdline'])
	#     except psutil.NoSuchProcess:
	#         pass
	#     else:
	#     	#processCommand = pinfo['cmdline']
	# 		#print (pinfo['cmdline'])
	# 		shell_command = pinfo['cmdline']
	# 		#print shell_command
	# 		if shell_command and 'python' in shell_command[0] and len(shell_command) > 0 and 'fermTempService.py' in shell_command[1]:
	# 			running = 1
	# 			break
	# 			os.system('kill %d' % os.getpid())

	#import subprocess
	#out=call(["ps", "aux"])
	out=check_output(["ps", "aux"])
	#print out
	#ipdb.set_trace()
	if 'fermtemp' in str(out):
		running = 1

	return running


if __name__ == "__main__":
	print get_system_state()
