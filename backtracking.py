from Data import Data
class Bt:
    def __init__(self , Matrix ,N , col, V , M,T=2):
        self.graph = Matrix
        self.m=M
        self.V=V
        self.T=T
        self.name=N
        self.cl=col

    def isSafe(self,graph, color):
        for i in range(self.V):
            for j in range(i, self.V):
                if graph[i][j]==1 and color[j]==color[i]:
                    return False
        return True

    def graphColoring(self,graph, m , i , color):
        if i==self.V:
            if self.isSafe(graph,color):
                self.printSolution(color)
                return True
            return False
        for j in range(1 , m+1):
            color[i]=j
            if self.graphColoring(graph , m , i+1 , color):
                return True
            color[i]=0
        return False

    def printSolution(self,color) :
        print("Solution Exists: Following are the assigned colors")
        for i in range(self.V):
            print(self.name[i]+" : "+self.cl[color[i]])

    def Start(self):
        color=list()
        for i in range(self.V):
            color.append(0)
        if not(self.graphColoring(self.graph,self.m,0,color)):
            print("Solution does not exist")

