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
    if inf  == sup:
        return None
    else:
        n = (((sup - inf)//2) + inf)
        while n+1 < sup and l[n] == l[n+1]:
            n += 1
        B = bintree.BinTree(l[n],None,None)
        B.left = __build_abr(inf,n,l)
        B.right = __build_abr(n+1,sup,l)
    return B


def Build_balanced_abr(l):
    '''
    Build a balanced abr
    '''
    fun.sort_bubble(l)
    n = len(l)
    B = __build_abr(0,len(l) - 1,l)
    return B


def Build_abr_asleaf (l):
    '''
    Build an non balanced abr
    '''
    n = len(l)
    B = add_leaf(None,1,l[0])
    for i in range (1,n):
        add_leaf(B,l[i])
    return B


##############################################################
##############################################################
##############################################################


def search(B,x):
    if B == None:
        return None
    else:
        if B.key == x:
            return B
        else:
            if x < B.key :
                return search(B.left,x)
            else:
                return search(B.right,x)

def serach_iter (B):
    while B != None and B.key != x:
        if x < B.left:
            B = B.left
        else:
            B = B.right
    return B

def add_leaf(B,x):
    if B == None:
        B = bintree.BinTree(x,None,None)
        return B
    else:
        if x <= B.key:
            B.left = add_leaf(B.left,x)
        else:
            B.right = add_leaf(B.right,x)
    return B

def __test_bin(B,inf,sup):
    if B == None:
        return True
    else:
        return B.key <= sup and B.key > inf and __test_bin(B.left,inf,B.key)\
            and __test_bin(B.right,B.key,sup)

def test_bin (B):
    if B == None:
        return False
    else:
        inf = -float("inf")
        sup = float("inf")
        return __test_bin(B,inf , sup)


def __delete_max (B,parent,x):
    if B.left == None and B.right == None:
        parent.left = None
    else:
        while B.right != None:
            parent = B
            print ("before" ,B.key)
            B = B.right
            print("after ", B.key)
        res = B.key
        if B.left != None:
            if parent.left == B:
                parent.left = B.left
            else:
                parent.right = B.left
        else:
            parent.right = None
        return res

def __delete (B,parent,x):
    if B == None:
        return B
    else:
        if x < B.key:
            return __delete(B.left,B,x)
        else:
            if x > B.key:
                return __delete(B.right,B,x)
            else:
                if B.left != None:
                    key = __delete_max(B.left,B,x)
                    B.key = key
                else:
                    if parent.left == B :
                        parent.left = B.right
                    else:
                        parent.right = B.right
    return B


def delete (B,x):
    if B == None:
        return B
    else:
        if x < B.key:
            return __delete(B.left,B,x)
        else:
            if x > B.key:
                return __delete(B.right,B,x)
            else:
                key = __delete_max(B.left,B,x)
                B.key = key
    return B

def delete_max (B):
    if B.right != None:
        B.right , res = delete_max(B.right)
    else:
        return B.left,B.key
    return B,res

def delete_rec (B,x):
    if B == None:
        return None
    else:
        if x == B.key:
            if B.right == None:
                return B.left
            else:
                if B.left == None:
                    return B.right
                else:
                    B.left , res = delete_max(B.left)
                    B.key = res
        else:
            if x < B.key:
                B.left = delete_rec(B.left,x)
            else:
                B.right = delete_rec(B.right,x)
    return B

def __coupe(x,B):
    if B == None:
        return (None,None)
    else:
        if B.key <= x :
            G = B
            G.right, D =__coupe(x,B.right)
        else:
            D = B
            G , D.left = __coupe(x,B.left)
    return G , D


def add_root (B,x):
    (G,D) = __coupe(x,B)
    return bintree.BinTree(x,G,D)



##############################################################
##############################################################
##############################################################

L = [0,1,2,3,4,5,6,7,8,9,10,31,32,33,34,35,36,37,38,39,66,67,68,69,70]
print("L ", L)
B = Build_balanced_abr(L)
print("list tree ",L)
print("tree B")
bintree.print_tree(B)
#delete_rec(B,54)
#print("delete 54 ")
#bintree.print_tree(B)
#print("delete 11")
#delete_rec(B,11)
#bintree.print_tree(B)
#print("delete 22")
#delete_rec(B,22)
#bintree.print_tree(B)
#print("delete 21")
#delete_rec(B,21)
#bintree.print_tree(B)
#print("added 27 ")
#add_leaf(B,27)
#bintree.print_tree(B)
#print("add root 30")
#B = add_root(B,30)
#bintree.print_tree(B)
#print("add root 25")
#B = add_root(B,25)
#bintree.print_tree(B)
