import bintree
import stack
import queue
import fun
from random import randint

M1 = [[17,24,1,8,15],
      [23,5,7,14,16],
      [4,6,13,20,22],
      [10,12,19,21,3],
      [11,18,25,2,9]]

def printmatrix(M):
    lignenbr = len(M)
    columnbr = len(M[0])
    for i in range (0,lignenbr):
        for j in range(0,columnbr):
            print(M[i][j],end = ' ')
        print()

#printmatrix(M1)

def initmatrix (l,c,val):
    res = []
    for i in range (l):
        res.append([])
        for j in range (c):
            res[i].append(val)
    return res

def buildmatrix(l,c,n):
    res = []
    for i in range (l):
        res.append([])
        for j in range (c):
            val = randint(0,n)
            res[i].append(val)
    return res

def prettymatrix (M):
    lignenbr = len(M)
    columnnbr = len(M[0])
    square_length = fun.evalsquare(M)+2
    interligne = fun.ligne_maker("-","-",square_length,columnnbr)
    blanklign = fun.ligne_maker(" ","|",square_length,columnnbr)
    print(interligne)
    for i in range (lignenbr):
        print(blanklign,end = '')
        print()
        print("|",end = '')
        for j in range (columnnbr):
            print(fun.center(str(M[i][j]),square_length) + "|",end = '')
        print()
        print(blanklign)
        print(interligne)




#B = initmatrix(8,4,8)
#print("B")
#printmatrix(B)
#print("A")
A = buildmatrix(100,30,10000)
#printmatrix(A)
#print (fun.evalsquare(A))

prettymatrix(A)

#f = load(filename)
#f.close()
#f.readlines ...
