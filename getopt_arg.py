# coding:utf-8

import sys
import getopt

argv = sys.argv[1:]

options,arguments = getopt.getopt(argv,"ab:",('apple','beans='))

for name,value in options:
	print('Name="%s", Value="%s"' % (name, value))

for argument in arguments:
	print('Argument="%s"' % argument)

# if name in ('-u','--username')

