import bintree
import queue
import stack
import fun
import bintd

def add_leaf(B,x):
    if B == None:
        B = bintree.BinTree(x,None,None)
        return B
    else:
        if B.key > x:
            if B.left == None:
                B.left = bintree.BinTree(x,None,None)
            else:
                add_leaf(B.left,x)
        else:
            if B.right == None:
                B.right = bintree.BinTree(x,None,None)
            else:
                add_leaf(B.right,x)
        return B

def __build_abr(inf,sup,l):
    if inf +1 == sup :
        return None
    n = (((sup - inf)//2) + inf)
    B = bintree.BinTree(l[n],None,None)
    if (n != inf) and not((inf + 1 == n) and (sup - 1 == n)):
        B.left = __build_abr(inf,n,l)
        B.right = __build_abr(n,sup,l)
    return B

def Build_balanced_abr(l):
    '''
    Build a balanced abr
    '''
    fun.sort_bubble(l)
    n = len(l)
    B = bintree.BinTree(l[n//2],None,None)
    B.left = __build_abr(0,n//2,l)
    B.right = __build_abr(n//2,n,l)
    return B

def Build_abr (l):
    '''
    Build an non balanced abr
    '''
    n = len(l)
    B = add_leaf(None,l[0])
    for i in range (1,n):
        add_leaf(B,l[i])
    return B


L = [12,3,4,5,72,6,8,54,34,51,64,43,2,23,32,78,47,21,22,37,9,90]
print("list before ",L)
C = Build_abr(L)
bintd.print_tree_int(C)
B = Build_balanced_abr(L)
print("list after ",L)
print("tree ")
bintd.print_tree_int(B)
B = add_leaf(B,79)
print("tree 2 ")
bintd.print_tree_int(B)
