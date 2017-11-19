import bintree
import queue
import stack
import fun
import bintd

##########################################################
##########################################################
##########################################################
# Builds

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

def Build_abr_asleaf (l):
    '''
    Build an non balanced abr
    '''
    n = len(l)
    B = add_leaf(None,l[0])
    for i in range (1,n):
        add_leaf(B,l[i])
    return B

##############################################################
##############################################################
##############################################################

def search(B,x):
    if B == None:
        return False
    else:
        if B.key == x:
            return True
        else:
            if x < B.key :
                return search(B.left,x)
            else:
                return search(B.right,x)

def add_leaf(B,x):
    if B == None:
        B = bintree.BinTree(x,None,None)
        return B
    else:
        if x <= B.key:
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

def __add_root (B,x,L,R):
    if B == None:
        L = None
        R = None
    else:
        if B.key <= x :
            L = B
            __add_root(B.right,x,L.right,R)
        else:
            R = B
            __add_root(B.left,x,L,R.right)


def add_root (B,x):
    L = bintree.BinTree(None,None,None)
    R = bintree.BinTree(None,None,None)
    L,R = __add_root(B,x,L,R)
    G = bintree.BinTree(x,L,R)





##############################################################
##############################################################
##############################################################

L = [12,3,4,5,72,6,8,54,34,51,66,10,3,4,21,23,456,453,23,12,345,66,54,22,2]
print("L ", L)
B = Build_balanced_abr(L)
print("list tree ",L)
print("tree B")
bintree.pretty_print_tree(B)
print(search(B,54))
print(search(B,6))
print(search(B,27))
add_root(B,21)
bintree.pretty_print_tree(B)
