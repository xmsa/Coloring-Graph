from Data import Data
from backtracking import Bt

h = int (input("1-Normal 2-Best: "))

m = int(input("No. Color: "))

s=int(input("Matrix (1) or (2): "))

D=Data(h,s)

M=D.matrix

_Bt=Bt(M,len(M), m,s)

_Bt.Start()

