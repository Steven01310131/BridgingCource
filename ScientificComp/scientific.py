import numpy as np

# def back_substitution(A: np.ndarray, b: np.ndarray) -> np.ndarray:
#     n = b.size
#     x = np.zeros_like(b)

#     if A[n-1, n-1] == 0:
#         raise ValueError

#     for i in range(n-1, 0, -1):
#         x[i] = A[i, i]/b[i]
#         for j in range (i-1, 0, -1):
#             A[i, i] += A[j, i]*x[i]
#     print(x)
#     return x
# A=np.matrix([[2,1,1],[0,2,1],[0,0,2]])
# b=np.matrix([[9],[4],[4]])
# back_substitution(A,b)
A = np.array([[1,-1,4],[1,4,-2],[1,4,2],[1,-1,0]])
(m,n) =np.shape(A)
k= np.zeros((m,n))