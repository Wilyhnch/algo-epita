import bintree
import ABR

def __copywithsize (B):
    if B == None:
        return (None,0)
    else:
        A = bintree.Bintree_Size(B.key,None,None,0)
        A.left , Sl = __copywithsize(B.left)
        A.right , Sr = __copywithsize(B.right)
        A.size = 1 + Sl + Sr
        return (A, A.size)

def copywithsize(B):
    A,size = __copywithsize(B)
    return A

def addwithsize(B,x):
    if B == None:
        B = bintree.Bintree_Size(x,None,None,1)
    else:
        B.size += 1
        if x > B.key:
            B.right = addwithsize(B.right,x)
        else:
            B.left = addwithsize(B.left,x)
    return B

def __nthBST (B,k,Found):
    if B == None :
        return (None,k,False)
    else:
        B.left,k,Found = __nthBST(B.left,k,Found)
        k = k - 1
        if k == 0 or Found :
            A = B
            return (A,0,True)
        else:
            B.right,k,Found = __nthBST(B.right,k,Found)
    return (B,k,Found)

def nthBST (B,k):
    if B == None:
        return None
    else:
        A,k,Found = __nthBST(B,k,False)
        return A



L = [1,2,3,4,5,6,7,8,9,10,31,32,33,34,35,36,37,38,39,66,67,68,69,70]
print("L ", L)
B = ABR.Build_balanced_abr(L)
print("list tree ",L)
print("tree B")
bintree.print_tree(B)
A = copywithsize(B)
bintree.print_tree(A)
C = nthBST(A,3)
print (C.key)
