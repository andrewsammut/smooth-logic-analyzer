#!/usr/bin/env python

import time
import serial
import sys
import os

os.remove('data.txt')

ser = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate = 115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

xcount = 0

while 1:
    # Reads one byte of informaiton constantly polling the serial port
    r=ser.read(8)
    
    # Blocks the '' instances of reading nothing
    if r > bytes(0b1):
        ex = open('data.txt', 'a')
        
        #Prints what was read from the serial port
        print(r)

        #Convert the Binary value of "bytes" data type to an int binary
        h = int(r,2)
        count = 0 

        # Loop through and split up the byte into its individual 1's and 0's and 
        # store in a file each 1 and zero on seperate lines
        for power in [1,2,4,8,16,32,64,128]:
            
            s = (str(xcount) + "," + str((h&(0x1<<count))/(power)) + "\n")
            ex.write(s)
            count = count + 1
            xcount = xcount + 1 
        ex.close()

    #else
        #s = (str(xcount) + "," + "0"        
            
