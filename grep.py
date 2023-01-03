#!/usr/bin/env python3
import os
#filename="log_final_"
storefile="grep_oahd"

#f=open(storefile, 'a')

for i in range(0,808):
	filename="log_final_"
	command=""
	filename=filename+str(i)
	#print(filename)
	command='cat '+filename+' | grep "oahd" >> grep_oahd'
	print(command)
	os.system(command)




