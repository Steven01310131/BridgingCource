import numpy.matlib
import numpy as np
import matplotlib.pyplot as plt
import math
#Given Functions 
def UniformGen(a,b,N):
    U = np.random.uniform(a,b, N)
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
def NormalGen(mu, sigma2, N):
    U1 =  UniformGen(0,1,N)
    U2 =  UniformGen(0,1,N)
    X = np.sqrt(-2*np.log(U1))*np.cos(2*np.pi*U2)
    X = mu + np.sqrt(sigma2)*X
    return X
def MultiNormalGen(mu, Sigma, N):
    dim = len(mu)
    Z = X = np.zeros([dim,N])
    B = np.linalg.cholesky(Sigma)
    for d in range(dim):
        Z[d,:] = NormalGen(0, 1, N)
    X = np.matlib.repmat(mu, N, 1).T + np.matmul(B,Z)
    return X
def McMcRandWalkGen(pdf, X0, SigmaWalk, N):
    dim = len(X0)
    X = np.zeros([dim,N])
    X[:,0] = X0
    for t in range(N-1):
        Z = MultiNormalGen(np.zeros(dim),SigmaWalk,1).T
        Y = X[:,t] + Z
        Xt = np.array([X[:,t]])
        Alfa = min(pdf(Y)/pdf(Xt),1)
        U = UniformGen(0,1,1)
        if U <= Alfa:
            X[:,t+1] = Y
        else:X[:,t+1] = X[:,t]
    return X



# 4 3 
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

#4.5
def betaB(b,N):
    U = UniformGen(0,1,N)
    X = 1-U**(1/b)
    return X

def betaA(a,N):
    U = UniformGen(0,1,N)
    X = U**(1/b)
    return X

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

#Miniproject 6.1
N=[100,200,500,1000,5000,10000,100000,1000000]
results=[]
for n in N :
    U=UniformGen(0,1,n)
    W=-2*np.log(U/2)
    G=W**2-W
    results.append(np.mean(G))
print(results)


# # for n in N:
# #     U=UniformGen(0,1,n)
# #     w=-np.log(U)
# #     G=np.cos(w)
# #     results.append(np.mean(G))
# # print(results)

# Metropolis Hastings

c = 1/20216.335877
f = lambda x: c*np.exp(-(x[0,0]**2*x[0,1]**2+x[0,0]**2+x[0,1]**2-8*x[0,0]-8*x[0,1])/2)
h=lambda x: x[0,0]*x[0,1]
Sigma = 2*np.eye(2)
Hhat = np.zeros(4)
for k in range(4):
    N = 10**(k+3)
    X0 = [0,0]
    X = McMcRandWalkGen(f, X0, Sigma, N)
    Hhat[k] = 1/N*np.sum(X[0,:]*X[1,:])
print("MCMC estimates = ",np.round(Hhat,4))

# 5.3
def Diffusion(x0,h,mu,sigma,n):
    Y=np.zeros(n)
    t=np.linspace(0,h*n,n)
    Y[0]=x0
    for k in range(n-1):
        Z=NormalGen(0,1,1)
        Y[k+1]=Y[k]+mu*Y[k]*h+sigma*Y[k]*np.sqrt(h)*Z
    plt.title("Diffusion process")
    plt.ylabel("Y")
    plt.xlabel("t")
    plt.plot(t,Y)
    plt.show()

Diffusion(1,0.001,1,0.25,2000) #Brownian Motion a(t,x)=μ and b(t,x)=σ
Diffusion(1,0.001,0,1,2000)    #Wiener μ= 0 and σ= 1

