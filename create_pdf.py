# coding:utf-8

from reportlab.pdfgen import canvas

pdf_file = input('PDF file:')

canvas = canvas.Canvas(pdf_file)
canvas.drawString(100,500,'Hello World')

yesno = input('Register:yes or no:')
if yesno == 'yes':
	canvas.save()
	print('Finished Save')
elif yesno == 'no':
	print('Failed')
	quit()
else:
	print('Nothing')
	quit()


import os
import subprocess

pwd = os.getcwd()
print(pwd)

list_file = os.listdir()
for i in list_file:
	if i == pdf_file:
		subprocess.Popen('rifle',pdf_file)
	else:
		print('Not a PDF file')
	


