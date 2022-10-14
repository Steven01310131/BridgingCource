import numpy as np
import matplotlib.pyplot as plt
def f(t,y):
    return 1/(1+t**2)-2*(y**2)
def fexact(t):
    return t/(1+t**2)
def RK2(t0,y0,h):
    n=round(10/h)
    RKerr=[]
    y=y0
    for i in range(n):    
        k1=f(t0,y0)
        k2=f((t0+h), (y0+h*k1))
        y=y0+(k1+k2)*(h/2)
        t0=t0+h
        y0=y
        RKerr.append((abs(y0-fexact(t0)))/fexact(t0))
    return RKerr

def RK3(t0,y0,h):
    n=round(10/h)
    y=y0
    RKerr=[]
    for i in range(n):
        k1= f(t0,y0)
        k2 = f( (t0+h/2), (y0+k1*h/2) )
        k3 = f( (t0+h/2), (y0+2*k2*h-k1*h) )
        y= y0 + (k1+4*k2+k3)*(h/6)
        t0=t0+h
        y0=y
        RKerr.append((abs(y0-fexact(t0)))/fexact(t0))
    return RKerr
    
def RK4(t0,y0,h):
    n=round(10/h)
    y=y0
    RKerr=[]
    for i in range(n):
        k1=h*f(t0,y0)
        k2 = h*f( (t0+h/2), (y0+k1/2) )
        k3 = h*f( (t0+h/2), (y0+k2/2) )
        k4 = h*f(  (t0+h) ,  (y0+k3)  )
        y= y0 + (k1+2*k2+2*k3+k4)/6
        t0=t0+h
        y0=y
        RKerr.append((abs(y0-fexact(t0)))/fexact(t0))
    return RKerr


hstep=[0.2,0.1,0.05,0.025,0.0125,0.00625]
# ErrorRK2=[]
# # ErrorRK3=[]
# # ErrorRK4=[]
# for i in hstep:
#     plt.
#     plt.plot(RK2(0,0,i))
for i in hstep:
    plt.plot(RK2(0,0,i))
    plt.plot(RK3(0,0,i))
    plt.plot(RK4(0,0,i)) 
    plt.ylabel("Error")
    plt.show()   





