# coding:utf-8

import socket

default_timeout = socket.getdefaulttimeout() is None
print('Default:{0}'.format(default_timeout))

input_timeout = input('Timeout:')

int_input_timeout = int(input_timeout)

set_timeout = socket.setdefaulttimeout(int_input_timeout)

get_timeout = socket.getdefaulttimeout()
print('Timeout:{0}'.format(get_timeout))


