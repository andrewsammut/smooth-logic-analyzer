import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib import style
#import serial
from threading import Thread
from queue import Queue
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from __future__ import print_function
import time
import random

import ftd2xx

BLOCK_LEN = 2048 * 32

pause = False
thread = False
xs = []
ys = []
global q, xcount, slide
q = Queue()
xval = 0
xcount = 0
x = 0

WINDOWSIZE = 50

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

dev = init()
print("\nDevice Details :")
print("Serial : " , dev.getDeviceInfo()['serial'])
print("Type : " , dev.getDeviceInfo()['type'])
print("ID : " , dev.getDeviceInfo()['id'])
print("Description : " , dev.getDeviceInfo()['description'])

#ser = serial.Serial(
#    port='/dev/ttyUSB0',
#    baudrate= 115200,
#    parity=serial.PARITY_NONE,
#    stopbits=serial.STOPBITS_ONE,
#    bytesize=serial.EIGHTBITS,
#    timeout=1
#)

def graph():
    global xval
    global pause

    if pause == False:
        print(q.qsize())
        
        if q.empty() == False:
            for line in range(q.qsize()):
                data = q.get_nowait()
                x,y = data.split(',')
                xs.append(float(x))
                ys.append(float(y))

        ax1.clear()
        ax1.plot(xs, ys, drawstyle='steps-pre')
    
        if len(xs) != 0: 
            scale(x)

    canvas.draw()

def readSerial():
    global xcount, pause, thread
    thread = True
    
    while 1:
        if pause == False:
            r=dev.read(1)

            if r > bytes(0b1):
                h = int(r,2)
                count = 0
                #print(r)
                for power in [1,2,4,8,16,32,64,128]:
                    s = (str(xcount) + "," + str((h&(0x1<<count))/(power)) + "\n")
                    q.put(s)
                    count = count + 1
                    xcount = xcount +1
            else:
                s = (str(xcount) + "," + "0")
                q.put(s)
                xcount = xcount +1

def main():
    global thread
    if thread == False: 
        t1 = Thread(target= readSerial)
        t1.daemon = True
        t1.start()
    graph()
    wind.after(50, main)

def scale(x):
    
    if (float(x) - xs[0]) <WINDOWSIZE:
        plt.xlim([0,float(x)])
    else:
        plt.xlim([(float(x) - WINDOWSIZE), float(x)])

def Pause():
    global pause
    global slide
    try:
        slide.destroy()
        xval = xs[-1]
        slide = tk.Scale(wind, from_=0, to=xval, length=700, orient='horizontal', command=slideValue)
        slide.set(xval)

    except:
        xval = xs[-1]
        slide = tk.Scale(wind, from_=0, to=xval, length=700, orient='horizontal', command=slideValue)
        slide.set(xval)
    
    if pause == True:
        pause = False
    else:
        pause = True
        slide.pack()

def slideValue(event):
    scale(slide.get())


wind = tk.Tk()
wind.geometry("800x500")
output_text = "Smooth logic analyzer \n"
wind.title("SmoothLogic")
input_frame=tk.Frame(wind, height=300, width=30, relief=tk.RAISED, bd=4)

style.use('fivethirtyeight')
fig = plt.figure(figsize=(8,3))
ax1 = fig.add_subplot(1,1,1)
plt.subplots_adjust(bottom=0.25)

tk.Button(wind, text="Quit", command=wind.quit).pack()

canvas = FigureCanvasTkAgg(fig, wind)
canvas.get_tk_widget().pack()
butt = tk.Button(master = wind, command=Pause, height=1, width=5, text = "Pause")
butt.pack()

main()
wind.mainloop()
