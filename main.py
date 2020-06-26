from Data import matrix ,createMatrix  , lst
from backtracking import Bt


m = int(input("No. Color: "))

s=int(input("Matrix (1) or (2): "))
if s==1:
    M = matrix
else :
    M=createMatrix(lst)

_Bt=Bt(M,len(M), m,s)

_Bt.Start()

