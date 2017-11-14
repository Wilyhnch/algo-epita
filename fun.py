#the goal of this file is to regroup all the small function seen in class

import bintree
import queue
import stack

#split function
def split (string,split = ' ',list_type = True):
    '''
    Function split (string, split, list_type)
    creates a list of sting or int by cutting the string at the split char
    string = intput string
    split = char (' ' by default)
    list_type = bool (output = list_str if True and list_int if False)(True by default)
    '''
    l = []
    res = ""
    if list_type:
        for c in string:
            if(c == split and res != ""):
                l.a.ppend(res)
                res = ""
            elif c != split:
                res += c
        if res != "":
            l.append(res)
    else:
        for c in string:
             if(c == split and res != ""):
                 l.append(int(res))
                 res = ""
             elif c != split:
                 res += c
        if res != "":
            l.append(int(res))
    return l
#print(split(testspace2,"w"))
#print(split(testspace,"w"))



#eval function
def eval (op,a,b):
    #print(op)
    return{
        '+' : a + b,
        '*' : a * b,
        '-' : a - b,
        '/' : a / b
        }.get(op,"opertator not found in eval")

#print(eval('+',2,3))
#print(eval('*',2,3))
#print(eval('-',2,3))
#print(eval('/',2,3))

def isop (c):
    return{
        '+' : True,
        '*' : True,
        '-' : True,
        '/' : True,
        '(' : True,
        ')' : True,
        }.get(c,False)

#print(isop('+'))
#print(isop(3))


#opertator eval
def opeval_at (op):
    return{
        '+' : 1,
        '*' : 2,
        '-' : 1,
        '/' : 2,
        '(' : 3,
        ')' : 0,
        }.get(op,"opertator not found in opeval")

def opeval(op1,op2):
    op_1 = opeval_at(op1)
    op_2 = opeval_at(op2)
    return op_1 < op_2

def printStack(S):
    T = stack.Stack()
    T = S
    print("[TOP]")
    while not(T.isempty()):
        print (T.pop(), " ")
    print ("[BOTTOM]")

#S = stack.Stack()
#S.push(1)
#S.push(2)
#S.push(3)
#printStack(S)

def evalsquare (M):
    ligne = len(M)
    column = len(M[0])
    length = 0
    for i in range (ligne):
        for j in range (column):
            res = str(M[i][j])
            if len(res) > length:
                length = len(res)
    return length

def center (s,l):
    switch = True
    while(len(s)<l):
        if switch:
            s = " " + s
            switch = False
        else:
            s += " "
            switch = True
    return s

def ligne_maker (filler, sep, length, column):
    res = sep
    for i in range (column):
        for j in range (length):
            res += filler
        res += sep
    return res

#print (ligne_maker(" ","|",6,8))
#print (ligne_maker("-","-",6,8))


def trim_str (string,front,nbr):
    res = ""
    length = len(string)
    if front:
        for i in range (nbr,length):
            res += string[i]
    else:
        for i in range (0,length - nbr):
            res += string[i]
    return res



#s = "this is a test"
#print(trim_str(s,True,3))
#print(trim_str(s,False,4))

def maxlist (l,rankfirst = 0):
    maxi = l[0]
    rankmax = rankfirst
    rank = rankfirst - 1
    for c in l:
        rank += 1
        if c > maxi :
            maxi = c
            rankmax = rank
    return (maxi , rankmax)

def len_queue (q):
    g = queue.Queue()
    g = q
    length = 0
    while not g.isempty():
        g.dequeue()
        length += 1;
    return length

def print_queue (b):
    q = queue.Queue()
    q = b
    res = "{"
    while not q.isempty():
        c = q.dequeue()
        if c ==None:
            print ("None}{")
        else:
            res += c.key + "}{"

    print (res)
