#! /usr/bin/env python
import sys

if len(sys.argv) > 1:
	env = sys.argv[1]
else:
	env = 'default'

if (env == 'pi'):
	MY_VAR = 'PI!!'
	ENV = 'pi'
else:
	MY_VAR = 'NO PI'
	ENV = 'nopi'

#print env