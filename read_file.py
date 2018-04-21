# coding: utf-8

#input.open.read

name = 'open filename:'

enter = input(name)

openfile = open(enter,'r')
readfile = openfile.read()

print(readfile)



