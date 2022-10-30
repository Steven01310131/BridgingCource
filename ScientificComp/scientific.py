from tkinter import W
import numpy as np
import matplotlib.pyplot as plt
import math

def UniformGen(a,b,N):
    U = np.random.uniform(a,b,size = N)
    return U

def ExpGen(lam,N):
    U=UniformGen(0,1,N)
    X=-1/lam*np.log(U)
    return X
def AcceptRejectGen(f, g, C, N, gGen, *arg_gGen):
    Z = np.zeros(N)
    for k in range(N):
        reject = True
        while reject:
            X = gGen(*arg_gGen,1)
            U =  UniformGen(0, 1, 1)
            if U <= f(X)/(C*g(X)):
                Z[k] = X
                reject = False
    return Z

# f = lambda x: 2*x
# g = lambda x: 1
# gGen = UniformGen
# arg_gGen = 0,1
# C = 2
# N = 5000
# X = AcceptRejectGen(f, g, C, N, gGen, *arg_gGen)
# plt.figure(figsize = (5, 3))
# plt.hist(X, bins = 30, histtype = "bar", color = "red", density = "true")
# x = np.linspace(0,1,200)
# plt.plot(x,f(x),linestyle ="-", color = "blue")
# plt.title("Histogram of $X$ and the pdf $f(x)$")
# plt.xlabel("$X$")
# plt.ylabel("Frequency %")
# plt.show()

f= lambda x:2/math.pi*np.sqrt(1-x**2)
g = lambda x: 1
gGen = UniformGen
arg_gGen = -1,1
C = 2
N = 5000
X = AcceptRejectGen(f, g, C, N, gGen, *arg_gGen)
plt.figure(figsize = (5, 3))
plt.hist(X, bins = 30, histtype = "bar", color = "red", density = "true")
x = np.linspace(-1,1,200)
plt.plot(x,f(x),linestyle ="-", color = "blue")
plt.title("Histogram of $X$ and the pdf $f(x)$")
plt.xlabel("$X$")
plt.ylabel("Frequency %")
plt.show()
















# plt.figure(figsize = (5,3))
# lam, N = 0.5, 50000
# X = ExpGen(lam,N)
# plt.hist(X, bins = 500, histtype = "bar", color = "red", density = "true")
# x = np.linspace(0,15,200)
# f = lam*np.exp(-lam*x)
# plt.plot(x,f,linestyle = "-", color = "blue")
# plt.title("Histogram of X and the pdf f(x)")
# plt.xlabel("X")
# plt.ylabel("Frequency %")
# plt.show()

#Miniproject 1
N=[100,200,500,1000,5000,10000,100000,1000000]
results=[]
for n in N :
    U=UniformGen(0,1,n)
    W=-2*np.log(U/2)
    G=W**2-W
    results.append(np.mean(G))
print(results)

# for n in N:
#     U=UniformGen(0,1,n)
#     w=-np.log(U)
#     G=np.cos(w)
#     results.append(np.mean(G))
# print(results)