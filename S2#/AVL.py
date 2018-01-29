import bintree
import stack
import avl
import ABR


#############################################################

# TP AVL

#############################################################

def __to_avl (B):
    if B == None:
        return None,-1
    else:
        A = avl.AVL(B.key,None,None,0)
        A.left , height_left = __to_avl(B.left)
        A.right , height_right = __to_avl(B.right)
        A.bal = height_left - height_right
        return A , 1 + max(height_left,height_right)


def to_avl (B):
    (A,_) = __to_avl (B)
    return A

def lr (A): #Rotation Gauche
    res = A.right
    A.right = res.left
    res.left = A
    A = res
    A.left.bal = -1 - A.bal
    A.bal = 1 + A.bal
    return A

def rr (A):
    aux = A.left
    A.left = aux.right
    aux.right = A
    A = aux

    A.right.bal = -1
    A.bal = 1 + A.bal
    return A

def lrr(A):
# left rotation on left child
    aux = A.left.right
    A.left.right = aux.left
    aux.left = A.left
# right rotation
    A.left = aux.right
    aux.right = A
    A = aux

    if A.bal == -1:
        (A.left.bal, A.right.bal) = (1, 0)
    elif A.bal == 1:
        (A.left.bal, A.right.bal) = (0, -1)
    else:
        (A.left.bal, A.right.bal) = (0, 0)
    A.bal = 0

    return A

def rlr(A):

    aux = A.right.left
    A.right.left = aux.right
    aux.right = A.right

    A.right = aux.left
    aux.left = A
    A = aux

    if A.bal == -1:
        (A.left.bal, A.right.bal) = (1, 0)
    elif A.bal == 1:
        (A.left.bal, A.right.bal) = (0, -1)
    else:
        (A.left.bal, A.right.bal) = (0, 0)
    A.bal = 0

    return A

def __insertAVL(x, A):
    if A == None:
        return (avl.AVL(x, None, None, 0), True)
    elif x == A.key:
        return (A, False)
    elif x < A.key:
        (A.left, dh) = __insertAVL(x, A.left)  # Recursive call, everything below in this branch is postorder
        if not dh:
            return (A, False)
        else:
            A.bal += 1  # When here, it means there has been a height change in left subtree
            if A.bal == 2:  # Only case when rotation is useful
                if A.left.bal == 1:
                    A = rr(A)
                else:
                    A = lrr(A)
            return (A, A.bal == 1)  # Only case when height has changed
    else:   # x > A.key
        (A.right, dh) = __insertAVL(x, A.right)
        if not dh:
            return (A, False)
        else:
            A.bal -= 1
            if A.bal == -2:
                if A.right.bal == -1:
                    A = lr(A)
                else:
                    A = rlr(A)

            return (A, A.bal == -1)

def insertAVL(x, A):
    (A, dh) = __insertAVL(x, A)
    return A


def maxBST(B):
    while B.right != None:
        B = B.right
    return B.key

def __deleteAVL(x, A):
    if A == None:
        return (None, False)
    elif x == A.key:
        if A.left != None and A.right != None:
            A.key = maxBST(A.left)
            x = A.key
        else:
            if A.left == None:
                return(A.right, True)
            else:
                return(A.left, True)
    if x <= A.key:
        (A.left, dh) = __deleteAVL(x, A.left)
        if not dh:
            return (A, False)
        else:
            A.bal -= 1
            if A.bal == -2:
                if A.right.bal == 1:
                    A = rlr(A)
                else:
                    A = lr(A)
            return (A, A.bal == 0)
        (A.right, dh) = __deleteAVL(x, A.right)
        if not dh:
            return (A, False)
        else:
            A.bal += 1
            if A.bal == 2:
                if A.left.bal == -1:
                    A = lrr(A)
                else:
                    A = rr(A)
            return (A, A.bal == 0)

def deleteAVL(x, A):
    (A, dh) = __deleteAVL(x, A)
    return A



########################################
#Preparation Fianl
########################################

def left(B,l = -1):
    if B == None:
        print('\n length=', l)
    else:
        print(B.key, end=' ')


def left_back_iter (B):
    s = stack.Stack()
    length = -1
    while B != None:
        s.push(B.key)
        B = B.left
    while not (s.isempty()):
        print(s.pop()," " , end = '')
        length += 1
    print ("\nlength = ",length)

def preorder (B):
    if B == None:
        return False
    else:
        print(B.key," ",end = '')
        preorder(B.left)
        preorder(B.right)

def preorder_iter(B):
    s = stack.Stack()
    if B != None:
        s.push(B)
        while not (s.isempty()):
            B = s.pop()
            print(B.key," ",end = '')
            if B.right:
                s.push(B.right)
            if B.left:
                s.push(B.left)

B = None
B = insertAVL(25,B)
print("25")
bintree.print_tree(B)
B = insertAVL(60,B)
print("60")
bintree.print_tree(B)
B = insertAVL(35,B)
print("35")

bintree.print_tree(B)
B = insertAVL(10,B)
print("10")

bintree.print_tree(B)
B = insertAVL(20,B)
print("20")

bintree.print_tree(B)
B = insertAVL(5,B)
print("5")

bintree.print_tree(B)
B = insertAVL(70,B)
print("70")

bintree.print_tree(B)
B = insertAVL(65,B)
print("65")

bintree.print_tree(B)
B = insertAVL(45,B)
print("45")

bintree.print_tree(B)
