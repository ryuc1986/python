#!/root/.pyenv/shims/python

import subprocess

print('Boot Application')

app = input('App:')

if app == 'nautilus':
	folder = input('Folder:')
else:
	folder = input('URL:')

subprocess.Popen([app,folder])


