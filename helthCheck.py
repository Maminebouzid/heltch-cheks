#!/usr/bin/env python3

import shutil
import psutil
import socket
def Healt_Check():
	problems=[]

	if psutil.cpu_percent(1) >80:
		problems.append("Error - CPU usage is over 80%")
	hdd = psutil.disk_usage('/')
	if int((hdd.free/hdd.total)*100)<20:
		problems.append("Error - Available disk space is less than 20%")
	if (psutil.virtual_memory().available*0.000001)<500:
		problems.append("Error - Available memory is less than 500MB")
	try:
		socket.gethostbyname("localhost")
	except :
		problems.append("Error - localhost cannot be resolved to 127.0.0.1")
	print(problems)

if __name__ == '__main__':
	Healt_Check()



