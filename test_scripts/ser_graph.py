#!/usr/bin/env python
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import serial
from threading import Thread
from queue import Queue
from matplotlib.widgets import Slider

WINDOWSIZE = 50

style.use('fivethirtyeight')

fig, ax1 = plt.subplots()
#fig = plt.figure()
#ax1 = fig.add_subplot(1,1,1)
#plt.subplots_adjust(bottom=0.35)

xs = []
ys = []


ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate= 115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

xcount = 0
x = 0

def readSerial(in_q):
    global xcount
    while 1:
        r=ser.read(8)
        
        if r > bytes(0b1):
            h = int(r,2)
            count = 0
            #print(r)
            for power in [1,2,4,8,16,32,64,128]:
                s = (str(xcount) + "," + str((h&(0x1<<count))/(power)) + "\n")
                in_q.put(s)
                count = count + 1
                xcount = xcount +1
        else:
            s = (str(xcount) + "," + "0")
            in_q.put(s)
            xcount = xcount +1


def animate(i):
    global xcount
    global x
    #graph_data = open('data.txt','r').read()
    #lines = graph_data.split('\n')
    print(q.qsize())

    if q.empty() == False:
        for line in range(q.qsize()):   
            data = q.get_nowait()
            x,y = data.split(',')
            xs.append(float(x))
            ys.append(float(y))

    #for line in lines:
    #    if len(line) > 1:
    #        x, y = line.split(',')
    #        xs.append(float(x))
    #        ys.append(float(y))
    ax1.clear()
    ax1.plot(xs, ys, drawstyle='steps-pre')
    
    if (float(x) - xs[0]) <WINDOWSIZE:
        plt.xlim([0,float(x)])
    else:
        plt.xlim([(float(x) - WINDOWSIZE), float(x)])
    

global q
q = Queue()
t1 = Thread(target = readSerial, args =(q,))
t1.daemon = True
t1.start()

ani = animation.FuncAnimation(fig, animate, interval=1)
plt.show()
