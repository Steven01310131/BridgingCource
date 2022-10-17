import math
from tkinter import Y 
import numpy as np
from numpy.linalg import inv,solve
import matplotlib.pyplot as plt
h=[0.1,0.05,0.025,0.0125,0.00625]

def fexact(t):
    x=np.linspace(0.01,1,num=999)
    return math.exp(-math.pi**2*t)*np.sin(math.pi*x)

dx=0.001
m=999
A=(np.diag(np.full(m,-2))+np.diag(np.ones(m-1),1)+np.diag(np.ones(m-1),-1))/dx**2

def f():
    x=np.linspace(0.01,1,num=999)
    return A@np.sin(math.pi*x).T
def Trap(h):
    B=(np.identity(m)-(h/2))*A
    C=(np.identity(m)+(h/2)*A)@f().T
    y1=np.linalg.solve(B,C)
    y0=y1
    y2=np.linalg.solve(B,C)
    return y1,y2

def BDF3(h,t0,t):
    n=round((t-t0)/h)
    y1,y2=Trap(h)
    y0=f()
    for i in range(n):
        y=np.linalg.inv((np.identity(m)-6*h*A/11))@((18/11)*y2-(9/11)*y1 + (2/11)*y0)
        y2=y
        y1=y2
        y0=y1
        t+=h
    return abs(y)
plt.plot(fexact(0.5))
plt.plot((BDF3(0.00625,0,0.5)))
plt.show()
# print(fexact())