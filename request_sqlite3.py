# coding:utf-8

import sqlite3

print('SQL Select Processing')

input_dbfile = input('Select DB:')
connect = sqlite3.connect(input_dbfile)
cursor = connect.cursor()

input_table = input('Select Table:')
sql = 'select * from {0}'.format(input_table)
cursor.execute(sql)

connect.commit

result = cursor.fetchall()

print(result)
 
#counter = sizeof(result)
#for i in counter:
#	print(result[i])

#resultone = cursor.fetchone()
#print(resultone)

cursor.close()


