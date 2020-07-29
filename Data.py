class Data:
    def __init__(self,h ,s):
        self.__namelist = [
            "Isfahan",
            "Yazd",
            "Fars",
            "Markazi",
            "Qom",
            "Chahar Mahaal and Bakhtiari",
            "Alborz",
            "Tehran",
            "Khorasan, Razavi",
            "Khorasan, North",
            "Khorasan, South",
            "Semnan",
            "Khuzestan",
            "Hamadan",
            "Mazandaran",
            "Kohgiluyeh and Boyer-Ahmad",
            "Bushehr",
            "Sistan and Baluchestan",
            "Hormozgān",
            "Golestan",
            "Kerman",
            "Qazvin",
            "Lorestan",
            "Ilam",
            "Kermanshah",
            "Kurdistan",
            "Zanjan",
            "Ardabil",
            "Azerbaijan, East",
            "Azerbaijan, West",
            "Gilan"]
        self.__namelist2=[
            "Isfahan Yazd",
            "Zanjan Qazvin Gilan",
            "Alborz Tehran Semnan Qom Golestan Mazandaran Markazi",
            "Ardabil",
            "Azerbaijan East, West",
            "Kurdistan Kermanshah Hamadan Ilam",
            "Chahar Mahaal and Bakhtiari Kohgiluyeh and Boyer-Ahmad Lorestan Khozestan",
            "Bushehr Fars",
            "Sistan and Baluchestan Kerman Hormozgān",
            "Khorasan, North Khorasan, Razavi Khorasan, South"
            ]
        self.cl=[
            'Red','Blue','Black','White','Green','Pink','Yellow','Gray','Rain']
        self.__lst2=[
            (1,3), (1,2), (1,4), (1,5), (1,6), (2,1),
            (2,6), (2,0), (2,9), (3,1), (3,4), (4,3),
            (4,1), (4,5), (5,4), (5,1), (5,6), (6,5),
            (6,1), (6,2), (6,0), (6,7), (7,6), (7,0),
            (7,8), (8,7), (8,0), (8,9), (9,2), (9,0),
            (9,8), (0,7), (0,8), (0,9), (0,2), (0,6)
            ]
        self.__lst1=[
            (0,1), (0,2), (0,15), (0,5), (0,22), (0,3), (0,4), (0,11), (0,10),
            (1,0), (1,2), (1,20), (1,10) ,
            (2,0), (2,1), (2,20), (2,18), (2,16), (2,15),
            (3,0), (3,22), (3,13), (3,21), (3,6), (3,7), (3,4),
            (4,0), (4,3), (4,7), (4,11),
            (5,0), (5,12), (5,22), (5,15),
            (6,3), (6,21), (6,7), (6,14),
            (7,6), (7,3), (7,4), (7,11), (7,14),
            (8,9), (8,11), (8,10),
            (9,8), (9,19), (9,11),
            (10,8), (10,11), (10,0), (10,1) ,(10,2), (10,20), (10,17),
            (11,0), (11,4), (11,7), (11,14), (11,19), (11,9), (11,8), (11,10), 
            (12,5), (12,23), (12,22), (12,15) ,(12,16),
            (13,3), (13,22), (13,24), (13,25), (13,26), (13,21),
            (14,6), (14,30), (14,21), (14,7), (14,11), (14,19),
            (15,5), (15,12), (15,0), (15,16), (16,12), (16,15), (16,2), (16,18),
            (17,10), (17,20), (17,18),
            (18,2), (18,16), (18,20), (18,17),
            (19,14), (19,11), (19,9),
            (20,1), (20,2), (20,18), (20,17), (20,10),
            (21,3), (21,6), (21,14), (21,30), (21,26), (21,13),
            (22,24), (22,13), (22,3), (22,0), (22,5), (22,12), (22,13),
            (23,24), (23,22), (23,12),
            (24,23), (24,22), (24,13), (24,25),
            (25,24), (25,13), (25,26), (25,29),
            (26,25), (26,29), (26,28), (26,27), (26,30), (26,21), (26,13),
            (27,28), (27,26), (27,30),
            (28,29), (28,26), (28,27),
            (29,25), (29,26), (29,28),
            (30,27), (30,26), (30,21), (30,14)
            ]
        self.matrix , self.name=self.__start(h , s)
        
    def __start(self,h , s):
        D=self.__lst1
        N=self.__namelist
        if s == 2:
            D=self.__lst2
            N=self.__namelist2

        M = self.__createMatrix(D)
        if h== 2:
            M , N = self.__sort(M ,N)
        if h== 3:
            M , N = self.__rsort(M , N)
        return M ,N

    def __createMatrix(self,lst):
        b=dict()
        c=0
        for i in range (len(lst)):
            m = True
            n = True
            for j in b:
                if b[j]==lst[i][1]:
                    n=False
                if b[j]==lst[i][0]:
                    m=False
            if m:
                b[c]=lst[i][0]
                c+=1
            if n: 
                b[c]=lst[i][1]
                c+=1
        m=list()
        for i in range(len(b)):
            m.append(0)
        matrix=list()
        for j in range(len(b)):
            matrix.append(m.copy())

        for i in lst:
            matrix[i[0]][i[1]]=1
        return matrix

    def __move (self,matrix  , N, m , n):
        yal=list()

        a=N[n]
        N[n]=N[m]
        N[m]=a

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if not 0 == matrix[i][j]:
                    yal.append((i,j))
        yal2=list()
        for i in yal:
            x,y=i
            if i[0]==m:
                x=n
            elif i[0]==n:
                x=m
            if i[1]==m:
                y=n
            elif i[1]==n:
                y=m
            yal2.append((x,y))
        matrix2=matrix[:]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix2[i][j]=0
        for i in yal2:
            x,y=i
            matrix2[x][y]=1
        return matrix2

    def __yal(self,matrix):
        M=list()
        for i in matrix :
            c=0
            for	j in i:
                if j>0:
                    c+=1
            M.append(c)
        return M

    def __sort(self,matrix , N):
        l=self.__yal(matrix)
        for i in range(len(l)):
            j=i+1
            while j<len(l):
                if l[i]<l[j]:
                    matrix=self.__move(matrix , N , i , j)

                    l=self.__yal(matrix)
                j+=1
        return matrix , N
    def __rsort(self,matrix,N):
        l=self.__yal(matrix)
        for i in range(len(l)):
            j=i+1
            while j<len(l):
                if l[i]>l[j]:
                    matrix=self.__move(matrix , N , i , j)
                    
                    l=self.__yal(matrix)
                j+=1
        return matrix , N
