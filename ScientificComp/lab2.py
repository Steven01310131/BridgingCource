import matplotlib.pyplot as plt
import numpy as np
 
A=np.array([[1,-1,1], [1, -0.5,0.25],[1,0,0], [1, 0.5,0.25],[1,1,1] ])
y=[[1],[0.5],[0],[0.5],[2]]
At=np.transpose(A)
AtA=np.matmul(At,A)
Aty=np.matmul(At,y)
c1=np.linalg.solve(AtA,Aty)
print(c1)

#solve equation LT*L*c=LT*b for c 
def ForBackSub(L,U,b):
    n=len(L)
    y=np.zeros(n)
    x=np.zeros(n)

    for i in range(n):#forward sub
        y[i]=((b[i]-np.sum(L[i,:i]*y[:i])))/L[i,i]
    for i in range(n-1,-1,-1):#backwards
        x[i]=(y[i]-np.sum(U[i,i+1:n]*x[i+1:n]))/U[i,i] 
    print(x)
    return x   
L1=np.linalg.cholesky(AtA)
L2=np.transpose(L1)
b=[[1],[0.5],[0],[0.5],[2]]
ForBackSub(L1,L2,Aty)
x=[-1,-0.5,0,0.5,1]
y=[1,0.5,0,0.5,1]