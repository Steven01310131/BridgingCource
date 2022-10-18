import math
from tkinter import Y
from turtle import title 
import numpy as np
from numpy.linalg import inv,solve,norm
import matplotlib.pyplot as plt

def f():
    x=np.linspace(0.01,1,num=m)
    return np.sin(math.pi*x).T
def Trap(h,y0,A):
    y1=inv(np.eye(m)-h/2*A) @ (h/2*A+np.eye(m)) @ y0
    return y1

def BDF3(h,t0,t,y0,y1,y2,A):
    n=round((t-t0)/h)
    Binv=inv(np.eye(m)-6/11*h*A)  
    for i in range(n):
        R = (18/11*y2-9/11*y1 + 2/11*y0)
        y3=Binv@R
        y0=y1
        y1=y2
        y2=y3
        t+=h
    return y3

h=[0.1,0.05,0.025,0.0125,0.00625]

def fexact(t):
    x=np.linspace(0.01,1,num=m)
    return np.exp(-1*(np.pi**2)*t)*np.sin(np.pi*x)

dx=0.001
m=1000 
A=(np.diag(np.full(m,-2))+np.diag(np.ones(m-1),1)+np.diag(np.ones(m-1),-1))/dx**2
err=[]
order=[]
for i in h:
    y0=f()
    y1=Trap(i,y0,A)
    y2=Trap(i,y1,A)
    p=BDF3(i,0,0.5,y0,y1,y2,A)
    err.append(norm(p-fexact(0.5)))
print(err)
for i in range(len(err)-1):
    l=math.log2(err[i])-math.log2(err[i+1])
    order.append(l)
print(order)
print("Order of conv for BDF3="+str(order[-1]))
plt.show()
"""
The theoretical order of convergence is 3 but i get a very low 0.4684838718894695
So there must be an error in my code but i cant find it 
"""

