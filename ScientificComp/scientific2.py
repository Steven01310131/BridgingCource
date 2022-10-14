import numpy as np

def givens_rotation(A):
    (num_rows, num_cols) = np.shape(A)
    
    Q = np.identity(num_rows)
    R = np.copy(A)

    
    (rows, cols) = np.tril_indices(num_rows, -1, num_cols)

    for (row, col) in zip(rows, cols):


        if R[row, col] != 0:
            (c, s) = givensparameters(R[col, col], R[row, col])

            G = np.identity(num_rows)
            G[row, row] = c
            G[col,col]=c
            G[row, col] = s
            G[col, row] = -s
            print(G)
            print()
            R = np.dot(G, R)
            print(R)
            print()
            Q = np.dot(Q, G)
    print(Q)
    print(R)
    return (Q, R)


def givensparameters(a, b):
    r = np.sqrt(a**2+b**2)
    c = a/r
    s = -b/r

    return (c, s)





