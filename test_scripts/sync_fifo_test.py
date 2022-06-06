from __future__ import print_function
import time
import random

import ftd2xx

BLOCK_LEN = 2048 * 32

def init():
 dev = ftd2xx.openEx(b'FT7OUAO9',1)
 time.sleep(0.1)
 dev.setTimeouts(5000, 5000)
 time.sleep(0.1)
 dev.setBitMode(0xff, 0x00)
 time.sleep(0.1)
 dev.setBitMode(0xff, 0x40)
 time.sleep(0.1)
 dev.setUSBParameters(0x10000, 0x10000)
 time.sleep(0.1)
 dev.setLatencyTimer(2)
 time.sleep(0.1)
 dev.setFlowControl(ftd2xx.defines.FLOW_RTS_CTS, 0, 0)
 time.sleep(0.1)
 dev.purge(ftd2xx.defines.PURGE_RX)
 time.sleep(0.1)
 dev.purge(ftd2xx.defines.PURGE_TX)
 time.sleep(0.1)
 return dev

tx_data = str(bytearray([ random.randrange(0, 256) for i in range(BLOCK_LEN)]))

dev = init()
print("\nDevice Details :")
print("Serial : " , dev.getDeviceInfo()['serial'])
print("Type : " , dev.getDeviceInfo()['type'])
print("ID : " , dev.getDeviceInfo()['id'])
print("Description : " , dev.getDeviceInfo()['description'])
print("\nWriting %d KB of data to the deivce..." % (BLOCK_LEN / 1024))
ts = time.time()
written = dev.write(tx_data)
print("\nReading %d KB of data from the deivce..." % (BLOCK_LEN / 1024))
rx_data = dev.read(BLOCK_LEN)
print(rx_data)
te = time.time()
 
p = te - ts 
print("\nComparing data...\n")
if (tx_data == rx_data):
 print("Data written matches the data read\n")
else:
 print("Data verification failed\n") 
 
dev.close()
print("Transfer Time = %.3f seconds" % p)
speed = (BLOCK_LEN / 1024./1024 / p)
print("Transfer Rate = %.3f MB/s" % speed)

print("\nSynchronous Test Finished Successfully!\nThank You!!")
