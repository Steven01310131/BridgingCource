import numpy as np
import scipy
from scipy import optimize
from scipy import linalg
import matplotlib.pyplot as plt
import rogues
# plt.style.use('seaborn-poster')
# x = np.linspace(0, 1, 101)
# y = 1 + x + x * np.random.random(len(x))
# A = np.vstack([x, np.ones(len(x))])
# print(A)
A = np.array([[1,-1,2,0],[1,2,-1,3],[1,1,0,2],[1,-1,2,0],[1,3,-1,4]])
b=np.array([[1],[-1],[0],[1]])
def QRcPivotlibrary(A):
    (Q,R,P)=scipy.linalg.qr(A,pivoting=True)
    rank=np.linalg.matrix_rank(A)
    return Q,R,P,rank

def LeastSquaresQRcPivot(A,b):
    (Q,R,P,rank)=QRcPivotlibrary(A)
    Q1=Q[:,:rank]
    R1=R[:rank,:rank]
    L=np.matmul(Q1,b[:rank,:])
    y=np.zeros(rank)
    x=np.zeros(len(b))
    for i in range(rank-1,-1,-1):#backwards
        y[i]=(L[i]-np.sum(R1[i,i+1:rank]*y[i+1:rank]))/R[i,i]
    x[:rank]=y
    for i in P:
        x[[0,i]] = x[[i, 0]]
    return x
    
x=LeastSquaresQRcPivot(A,b)
print(x)
print(np.linalg.norm(np.matmul(A,x)-b,2))
