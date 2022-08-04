import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib import style
import serial
from threading import Thread
from queue import Queue
import time
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

pause = False
thread = False
thread2 = False
xs = []
ys = []
xss = []
yss = []
global q, xcount, slide, qw, slide2
q = Queue()
qw = Queue()
xval = 0
xcount = 0
xcount2 = 0
x = 0
xx = 0

WINDOWSIZE = 50

serr = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate= 115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
serw = serial.Serial(
        port='/dev/ttyS0',
        baudrate=115200)

def graph():
    global xval
    global pause
    if pause == False:
        #print(q.qsize())
        print(qw.qsize())
        if q.empty() == False:
            for line in range(q.qsize()):
                data = q.get_nowait()
                x,y = data.split(',')
                xs.append(float(x))
                ys.append(float(y))
        if qw.empty() == False:
            for line2 in range(qw.qsize()):
                data2 = qw.get_nowait()
                xx,yy = data2.split(',')
                xss.append(float(xx))
                yss.append(float(yy))
        ax2.clear()
        ax1.clear()
        ax1.plot(xs, ys, drawstyle='steps-pre')
        ax2.plot(xss, yss, drawstyle='steps-pre')
    
        if len(xs) != 0: 
            scale(x)

        if len(xss) != 0: 
            scale2(xx)

    canvas.draw()
    canvas2.draw()

def readSerial():
    global xcount, pause, thread
    thread = True
    
    while 1:
        if pause == False:
            r=serr.read(8)

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

def writeSerial():
    global thread2, xcount2
    thread2 = True
    i=0
    counter = 0
    # rdata = [42, 54]
    # Include a function that will write a value to uart Port
    # Next function will then write teh same info to a queue
    while 1: 
        if pause == False:
            serw.write(str(counter).encode())
            data = bin(counter)
            conv = int(data,2)
            count = 0
            for power in [1,2,4,8,16,32,64,128]:
                s = (str(xcount2) + "," + str((conv&(0x1<<count))/(power)) + "\n")
                qw.put(s)
                count = count + 1
                xcount2 = xcount2 + 1
                #print(s)
            if counter == 100:
                counter = 0
            else:
                counter = counter + 1
            time.sleep(0.01)
    

def main():
    global thread
    if thread == False: 
        t1 = Thread(target= readSerial)
        t1.daemon = True
        t1.start()
    if thread2 == False:
        t2 = Thread(target=writeSerial)
        t2.daemon = True
        t2.start()
    graph()
    wind.after(50, main)


def scale(x): 
    if (float(x) - xs[0]) <WINDOWSIZE:
        ax1.set_xlim([0,float(x)])
    else:
        ax1.set_xlim([(float(x) - WINDOWSIZE), float(x)])

def scale2(x):
    if (float(x) - xss[0]) <WINDOWSIZE:
        ax2.set_xlim([0,float(x)])
    else:
        ax2.set_xlim([(float(x) - WINDOWSIZE), float(x)])


def Pause():
    global pause
    global slide
    global slide2
    try:
        slide.destroy()
        slide2.destroy()
        xval = xs[-1]
        xxval = xss[-1]
        slide = tk.Scale(wind, from_=0, to=xval, length=700, orient='horizontal', command=slideValue)
        slide.set(xval)
        slide2 = tk.Scale(wind, from_=0, to=xxval, length=700, orient='horizontal', command=slideValue2)
        slide2.set(xxval)

    except:
        xval = xs[-1]
        xxval = xss[-1]
        slide = tk.Scale(wind, from_=0, to=xval, length=700, orient='horizontal', command=slideValue)
        slide.set(xval)
        slide2 = tk.Scale(wind, from_=0, to=xxval, length=700, orient='horizontal', command=slideValue2)
        slide2.set(xxval)

    if pause == True:
        pause = False
    else:
        pause = True
        slide.pack()
        slide2.pack()

def slideValue(event):
    scale(slide.get())

def slideValue2(event):
    scale2(slide2.get())


wind = tk.Tk()
wind.geometry("800x500")
output_text = "Smooth logic analyzer \n"
wind.title("SmoothLogic")
input_frame=tk.Frame(wind, height=300, width=30, relief=tk.RAISED, bd=4)

style.use('fivethirtyeight')
fig = plt.figure(figsize=(8,1.35))
fig2 = plt.figure(figsize=(8,1.35))
ax1 = fig.add_subplot(1,1,1)
ax2 = fig2.add_subplot(1,1,1)
plt.subplots_adjust(hspace=0.6, wspace=0.6, bottom=0.2)

tk.Button(wind, text="Quit", command=wind.quit).pack()

canvas = FigureCanvasTkAgg(fig, wind)
canvas2 = FigureCanvasTkAgg(fig2, wind)
canvas.get_tk_widget().pack()
canvas2.get_tk_widget().pack()
butt = tk.Button(master = wind, command=Pause, height=1, width=5, text = "Pause")
butt.pack()

main()
wind.mainloop()
