from cmath import exp
import math
import matplotlib.pyplot as plt
from numpy.linalg import inv,solve,norm
import numpy as np

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
def errorplots(Numerical_method,f,fe,initial):#function to compute the relative errors and the order of convergence initial is to specify the initial conditions 
    err=[]
    order=[]
    for i in h:
        err.append(norm(Numerical_method(0,initial,i,10,f)-fe(10)))
    for i in range(len(err)-1):
        l=math.log2(err[i]/err[i+1])/(h[i+1]/h[i])
        order.append(l)
    print(f"Order of convergence with the  {Numerical_method.__name__} method of the function {f.__name__}={str(order[-1])}")
    return err
# commands to plot the errors with euler 
a=errorplots(euler,fa,fa_exact,1)
b=errorplots(euler,fb,fb_exact,0)
c=errorplots(euler,fc,fc_exact,1)

fig,ax=plt.subplots(3)
fig.suptitle('For euler method ')
ax[0].loglog(h,a)
ax[0].set_title("For function a")
ax[2].set(xlabel="step sizes h")
ax[1].loglog(h,b)
ax[1].set_title("For function b")
ax[2].loglog(h,c)
ax[2].set_title("For function c")
for i in range(3):
    ax[i].set(ylabel="Relative error")
plt.show()

def euler_implicit(t0,y0,h,t,f):
    n=round((t-t0)/h)
    for i in range(n):
        y=y0+h*f(t0+h,y0+h*f(t0,y0))
        y0=y
        t0+=h
    return y
a=errorplots(euler_implicit,fa,fa_exact,1)
b=errorplots(euler_implicit,fb,fb_exact,0)
c=errorplots(euler_implicit,fc,fc_exact,1)

fig,ax=plt.subplots(3)
fig.suptitle('For euler implicit method ')
ax[0].loglog(h,a)
ax[0].set_title("For function a")
ax[2].set(xlabel="step sizes h")
ax[1].loglog(h,b)
ax[1].set_title("For function b")
ax[2].loglog(h,c)
ax[2].set_title("For function c")
for i in range(3):
    ax[i].set(ylabel="Relative error")
plt.show()

def trapezoid(t0,y0,h,t,f):
    n=round((t-t0)/h)
    for i in range(n):
        y=y0+(h/2)*(f(t0,y0)+f(t0+h,y0+h*f(t0,y0)))
        y0=y
        t0+=h
    return y

a=errorplots(trapezoid,fa,fa_exact,1)
b=errorplots(trapezoid,fb,fb_exact,0)
c=errorplots(trapezoid,fc,fc_exact,1)

fig,ax=plt.subplots(3)
fig.suptitle('For trapezoid method ')
ax[0].loglog(h,a)
ax[0].set_title("For function a")
ax[2].set(xlabel="step sizes h")
ax[1].loglog(h,b)
ax[1].set_title("For function b")
ax[2].loglog(h,c)
ax[2].set_title("For function c")
for i in range(3):
    ax[i].set(ylabel="Relative error")
plt.show()  

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
def Taylor_errorplots(Numerical_method,fe):#function to compute the relative errors and the order of convergence for the taylor
    err=[]
    order=[]
    for i in h:
        err.append(norm(Numerical_method(0,0,i,10,fbtaylor2,fbtaylor3)-fe(10)))
    for i in range(len(err)-1):
        l=math.log2(err[i]/err[i+1])/(h[i+1]/h[i])
        order.append(l)
    print(f"Order of convergence with the  {Numerical_method.__name__} method of the function  is ={str(order[-1])}")
    return err
a=Taylor_errorplots(Taylor,fb_exact)
plt.title("For the Taylor method")
plt.loglog(h,a)
plt.xlabel("Step size h")
plt.ylabel("Error")
plt.show()  

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
for j in h:
    print(f"for step size h={j}")
    for i in range(1,6):
        print(f"The error at t={i} is error={norm(RK2(0,0,j,i,f4)-f4_exact(i))}")
err=[]
order=[]
h=[0.2,0.1,0.05,0.025,0.0125,0.00625]
for j in h:
    err.append(norm(RK2(0,0,j,5,f4)-f4_exact(5)))
for i in range(len(err)-1):
    l=math.log2(err[i]/err[i+1])/(h[i+1]/h[i])
    order.append(l)
print(f"Order of convergence is ={order}")