#!/usr/bin/env python
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import serial
from threading import Thread
from queue import Queue
from matplotlib.widgets import Slider, TextBox
import time

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate= 115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

pause = False 
global q
global wind
global xcount
q = Queue()
WINDOWSIZE = 50

style.use('fivethirtyeight')

fig, ax1 = plt.subplots()
plt.subplots_adjust(bottom=0.25)
xcount = 0
x = 0
global xs
xs = []
ys = []
#axx = plt.axes([0.3, 0.05, 0.4, 0.075]) 
 
def update(val):
    plt.xlim([(float(val) - WINDOWSIZE), float(val)])

#wind.on_changed(update)
#def submit(expression):
#    data = eval(expression)
#    tdata = int(data)
#    timeout = time.time() + tdata
#    print("unausing")
#    while True:
#        if time.time() > timeout:
#            pause = True
#            print("pausing")
#            break
#        else:
#            pause = False

def readSerial():
    global xcount
    global pause
    while 1:
        if pause == False:
            r=ser.read(8)
        
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

t1 = Thread(target = readSerial)
t1.daemon = True
t1.start()

def animate(i):
    print(q.qsize())
    global x
    global wind
    if q.empty() == False:
        for line in range(q.qsize()):   
            data = q.get_nowait()
            x,y = data.split(',')
            xs.append(float(x))
            ys.append(float(y))

    ax1.clear()
    ax1.plot(xs, ys, drawstyle='steps-pre')
    
    if (float(x) - xs[0]) <WINDOWSIZE:
        plt.xlim([0,float(x)])
    else:
        plt.xlim([(float(x) - WINDOWSIZE), float(x)])
 
    #wind = Slider(axx, 'scroll', 0, xcount, 0) 
    #wind.on_changed(update) 

def on_click(event):
    global pause
    global wind
    #(xm,ym),(xM,yM) = wind.label.clipbox.get_points()
    #if xm < event.x < xM and ym < event.y < yM:
    #    return
    #else:
    if pause == True:
        pause = False
    else:   
        pause = True

#text_box=TextBox(axbox, "pause")
#text_box.on_submit(submit)
#text_box.set_val("8") 
#axx = plt.axes([0.3, 0.05, 0.4, 0.075]) 
#wind = Slider(axx, 'scroll', 0, xcount, xcount) 
#wind.on_changed(update) 

fig.canvas.mpl_connect('button_press_event', on_click)
ani = animation.FuncAnimation(fig, animate, interval=1)
plt.show()
#pause = True
