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
        #while l[n] == l [n+1]:
        #    n += 1
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
            B = B.right
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

def find_max (B):
    while B.right != None:
        B = B.left
    return B

def delete_rec (B,x):
    if B == None:
        pass
    else:
        if x < B.key:
            B.left = delete_rec(B.left,x)
        else:
            if x > B.key:
                B.right = delete_rec(B.right,x)
            else:
                if B.right == None :
                    return B.left
                else:
                    if B.left == None:
                        return B.right
                    else:
                        if B.left == None and B.right == None:
                            return None
                        else:
                            res = find_max(B.left)
                            B.key = res.key
                            return delete_rec(B,res.key)
    return B





##############################################################
##############################################################
##############################################################

L = [17,3,1,5,72,6,7,56,34,11,66,10,26,2,4,21,24,456,453,23,12,345,54,22,8]
print("L ", L)
B = Build_balanced_abr(L)
print("list tree ",L)
print("tree B")
bintree.pretty_print_tree(B)
delete_rec(B,54)
print("delete 54 ")
bintree.pretty_print_tree(B)
print("delete 11")
delete(B,11)
bintree.pretty_print_tree(B)
print("delete 22")
delete(B,22)
bintree.pretty_print_tree(B)
print("delete 21")
delete(B,21)
bintree.pretty_print_tree(B)
print("added 25 ")
add_leaf(B,25)
bintree.pretty_print_tree(B)
