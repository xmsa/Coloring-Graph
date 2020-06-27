from Data import createMatrix  , lst1, lst2
from backtracking import Bt


m = int(input("No. Color: "))

s=int(input("Matrix (1) or (2): "))
if s==1:
    M = createMatrix(lst1)
else :
    M=createMatrix(lst1)

_Bt=Bt(M,len(M), m,s)

_Bt.Start()

