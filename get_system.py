# coding:utf-8

import os
print('---[Import OS]---')

loginname = os.getlogin()
print('LoginName:{0}'.format(loginname))

lsos = os.uname()[0]

if lsos == 'Linux' or 'Windows':
	print('OS:{0}'.format(lsos))
else: 
	print('Not Linux')

if lsos == 'Linux':
	cwd = os.getcwd()
	print('pwd:{0}'.format(cwd))


import platform as pf
print('\n---[Import Platform]---')

platform = pf.uname()
for i in list(platform):
	print(i)
###################################################
platformlist = ['node','system','release','version']

 oslib = []
for g in platformlist:
 oslib.append('os.{0}'.platform(g))

for i in platformlist:
 print('{0}: '.format(upper(platform)))
####################################################

node = pf.node()
print('Node:{0}'.format(node))

system = pf.system()
print('System:{0}'.format(system))

release = pf.release()
print('Release:{0}'.format(release))

version = pf.version()
print('Version:{0}'.format(version))
