import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib import style
import serial
from threading import Thread
from queue import Queue
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

thread = False
xs = []
ys = []
global q, xcount
q = Queue()
x = 0
xcount = 0

WINDOWSIZE = 50

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate= 115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

def graph():
    print(q.qsize())
    global x
    
    if q.empty() == False:
        for line in range(q.qsize()):
            data = q.get_nowait()
            x,y = data.split(',')
            xs.append(float(x))
            ys.append(float(y))

    ax1.clear()
    ax1.plot(xs, ys, drawstyle='steps-pre')
    canvas.draw()
    if len(xs) != 0:
        
        if (float(x) - xs[0]) <WINDOWSIZE:
            plt.xlim([0,float(x)])
        else:
            plt.xlim([(float(x) - WINDOWSIZE), float(x)])

def readSerial():
    global xcount, pause, thread
    thread = True
    
    while 1:
        #if pause == False:
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


def main():
    global thread
    if thread == False: 
        t1 = Thread(target= readSerial)
        t1.daemon = True
        t1.start()
    graph()
    wind.after(50, main)


wind = tk.Tk()
wind.geometry("800x500")

output_text = "Smooth logic analyzer \n"
output=""
crvar = tk.StringVar(wind)
crvar.set('')
quvar = tk.StringVar(wind)
quvar.set('')


wind.title("SmoothLogic")
input_frame=tk.Frame(wind, height=300, width=30, relief=tk.RAISED, bd=4)

style.use('fivethirtyeight')
fig, ax1 = plt.subplots()
plt.subplots_adjust(bottom=0.25)


#ax1.plot(xs,ys, drawstyle='steps-pre')
canvas = FigureCanvasTkAgg(fig,master = wind)  
canvas.get_tk_widget().pack()
#plotFrame = tk.Frame(master=wind, relief=tk.GROOVE, bd=4)
#plotFrame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
#lblplot=tk.Label(master=plotFrame, text="SmoothLogic Plot", font="Arial 16")
#lblplot.grid(row=0, column=0, padx=0, pady=5, sticky="nsew")


main()
wind.mainloop()
