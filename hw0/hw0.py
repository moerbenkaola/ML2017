import sys
import numpy as np

atxt = sys.argv[1]
btxt = sys.argv[2]
txt = sys.argv[3]
matrixa = np.loadtxt(atxt, delimiter=',')
matrixb = np.loadtxt(btxt, delimiter=',')
print matrixa.shape
print matrixb.shape
matrix = np.dot(matrixa, matrixb)
print matrix
sortmatrix = np.sort(matrix)
print sortmatrix
np.savetxt(txt,sortmatrix,fmt="%d")
