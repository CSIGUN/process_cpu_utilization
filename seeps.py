#!/opt/homebrew/bin/python3
import time
import os
import sys
from subprocess import PIPE, run
from datetime import datetime

def out(command):
	result = run(command, stdout=PIPE, stderr=PIPE, shell=True)
	return result.stdout

now = datetime.now()

if __name__ == "__main__":
	count = 0
	my_output=""

	print("start time: ",now.hour,"시 ",now.minute,"분")
	
	filename="./log_"

	while True:
		if count == 3600: #1min=60(1)
			break
		filename=filename+str(count)
		f = open(filename, 'a')

		my_output = str(out("ps aux"))
		f.write(my_output)
		count = count+1
		filename="./log_"
		time.sleep(1)

	print("The measure is finish")
	now = datetime.now()
	print("end time: ",now.hour,"시 ",now.minute,"분")

