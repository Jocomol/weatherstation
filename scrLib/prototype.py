import os, sys, time

while True:
	file = open('/sys/bus/w1/devices/28-00000833e8ff/w1_slave')
	filecontent = file.read()
	file.close
	value1 = filecontent.split("\n")
	value2 = value1[1]
	value3 = value2.split(" ")
	value4 = value3[9]
	value5 = value4.split("=")
	temp = float(value5[1])
	temp = temp / 1000
	print ("Es ist:",temp ,"°C Warm")
	time.sleep(1)
