from cmath import exp
import math
from tkinter import Y
import matplotlib.pyplot as plt
def fa(t,y):
    return t*math.exp(-t)-y
def fb(t,y):
    return math.cos(y)**2
def fc(t,y):
    return (t**3)/y

def fa_exact(t):
    return (1+0.5*t**2)*math.exp(-t)
def fb_exact(t):
    return 1/math.tan(t)
def fc_exact(t):
    return math.sqrt(0.5*t**4+1)

def euler(t0,y0,h,t,f):
    n=round((t-t0)/h)
    for i in range(n):
        y=y0+h*f(t0,y0)
        y0=y
        t0+=h
    return y
h=[0.2,0.1,0.05,0.025,0.0125,0.00625]

def errorplots(f,fe):
    lst=[]
    for i in h:
        lst.append(abs((euler(0,1,i,10,f)-fe(10))/fe(10)))
    print(lst)
    plt.plot(lst)
    plt.xlabel("step sizes h")
    plt.ylabel("Relative error")
    plt.show()

# errorplots(fa,fa_exact)
# errorplots(fb,fb_exact)
# errorplots(fc,fc_exact)
# def eulerimplicit(t0,y0,h,t,f):
#     n=round((t-t0)/h)
#     z=y0
#     for i in range():
def euler_implicit(t0,y0,h,t,f):
    n=round((t-t0)/h)
    for i in range(n):
        y=y0+h*f(t0+h,y0+h*f(t0,y0))
        y0=y
        t0+=h
    return y

def trapezoid(t0,y0,h,t,f):
    n=round((t-t0)/h)
    for i in range(n):
        y=y0+(h/2)*(f(t0,y0)+f(t0+h,y0+h*f(t0,y0)))
        y0=y
        t0+=h
    return y
# print(euler_implicit(0,1,0.2,10,fa))  
# print(fa_exact(10))     

def fbtaylor2(t,y):
    return math.cos(y)**2

def fbtaylor3(t,y):
    return -4*math.sin(y)*math.cos(y)**3

def Taylor(t0,y0,h,t,f2,f3):
    n=round((t-t0)/h)
    for i in range(n):
        y=y0 + h*f2(t0,y0)+h**2*f3(t0,y0)/2
        y0=y
        t0+=h
    return y

def RK2(t0,y0,h,t,f):
    n=round((t-t0)/h)
    for i in range(n):
        k1=f(t0,y0)
        k2=f((t0+h), (y0+h*k1))
        y=y0+(k1+k2)*(h/2)
        t0=t0+h
        y0=y
    return y 
def f4(t,y):
    return -y+t**0.1*(1.1+t)
def f4_exact(t):
    return t**1.1
# for j in h:
#     print("for h=",j,)
#     for i in range(5):
#         print("The error at t=",i+1,"is ",abs((RK2(0,0,j,i+1,f4)-f4_exact(i+1))/f4_exact(i+1)))
