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

def __delete_key (B,To_del):
    new_node = To_del
    while new_node.right != None:
        new_node = new_node.right
    To_del.key = new_node.key
    new_node = new_node.left
    return B



def delete_key (B,x):
    To_del = search (B,x)
    if To_del == None:
        return B
    else:
        parent = To_del
        if parent.left == None and parent.right == None:
            To_del = None
        else:
            C = To_del.left
            while C.right != None:
                parent = C
                C = C.right
                To_del.key = C.key
                if parent != To_del:
                    parent.right = C.left
                else:
                    parent.left = C.left
        return B







##############################################################
##############################################################
##############################################################

L = [17,3,1,5,72,6,7,56,34,51,66,10,26,11,2,4,21,24,456,453,23,12,345,54,22,8]
print("L ", L)
B = Build_balanced_abr(L)
print("list tree ",L)
print("tree B")
bintree.pretty_print_tree(B)
delete_key(B,54)
print("delete 54 ")
bintree.pretty_print_tree(B)
print("delete 11")
delete_key(B,11)
bintree.pretty_print_tree(B)
print("delete 22")
delete_key(B,22)
bintree.pretty_print_tree(B)
