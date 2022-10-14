from re import X
import numpy as np
import scipy
from scipy import optimize
from scipy import linalg
import matplotlib.pyplot as plt
x=np.array([[1],[2],[3],[4]])
print(x)
x[[0,1]] = x[[1, 0]]
print(x)