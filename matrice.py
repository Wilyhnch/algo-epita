#Matrices

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
            print(M[i][j])
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

def load_matrix(f_name):
    M = []
    f = open(f_name,"r")
    M_f = f.readlines()
    f.close()
    length = len(M_f)
    for i in range (length):
        tst = fun.trim_str(M_f[i],False,1)
        res = fun.split(tst,' ',False)
        M.append(res)
    return M

def add(A,B):
    l, c = (len(A),len(A[0]))
    if len(B)!= l and len(B[0])!= c :
        raise Exception ("matrices not the same size")
    M = initmatrix(l,c,0)
    for i in range (l):
        for j in range (c):
            M[i][j] = A[i][j] + B[i][j]
    return M


#B = initmatrix(8,4,8)
#print("B")
#printmatrix(B)
#print("A")
#A = buildmatrix(100,30,10000)
#printmatrix(A)
#print (fun.evalsquare(A))
#prettymatrix(A)
#f = load(filename)
#f.close()
#f.readlines ...
C = load_matrix("mat_text")
#print("C")
prettymatrix(C)
#print("M1")
#prettymatrix(M1)
#D = add(M1,C)
#prettymatrix(D)

def dynamatrix (I):
    M = I
    line = len(M)
    col = len(M[0])
    for i in range (1,line):
        for j in range (col):
            l = []
            l.append(M[i-1][j])
            if j > 0 :
                l.append(M[i-1][j-1])
            if j < (col - 1):
                l.append(M[i-1][j+1])
        best , r = fun.maxlist(l)
        M[i][j] += best
    return (fun.maxlist(M[line-1]),M)

def mathpath (M):
    line = len(M)
    col = len(M[0])
    best , rank = fun.maxlist(M[line-1])
    print("rank" , rank)
    s = stack.Stack()
    s.push(rank)
    ranked = False
    for i in range(line - 2,-1,-1):
        for j in range(col):
            l = []
            if j == rank or j == rank +1 or j == rank - 1:
                if not(ranked):
                    newrank = j
                l.append(M[i][j])
        best, rank = fun.maxlist(l,newrank)
        s.push(rank)
    return s

res , M2 = dynamatrix(C)
prettymatrix(M2)
path = mathpath(M2)
fun.printStack(path)
