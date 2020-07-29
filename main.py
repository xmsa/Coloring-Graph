from Data import Data
from backtracking import Bt

h = int (input("1-Normal 2-Sort 3-Reverse Sort: "))

m = int(input("No. Color: "))

s=int(input("Matrix (1) or (2): "))

D=Data(h,s)

M=D.matrix
N=D.name
C=D.cl
_Bt=Bt(M,N,C,len(M), m,s)

_Bt.Start()

