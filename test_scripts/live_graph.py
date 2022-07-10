#!/usr/bin/env python
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import serial

WINDOWSIZE = 50


style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    
    graph_data = open('data.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    ax1.clear()
    ax1.plot(xs, ys, drawstyle='steps-pre')
    if (float(x) - xs[0]) < WINDOWSIZE:
        plt.xlim([0,float(x)])
    else:
        plt.xlim([(float(x)-WINDOWSIZE), float(x)])

ani = animation.FuncAnimation(fig, animate, interval=1)
plt.show()
