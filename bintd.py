import bintree
import queue
import stack
import fun



def size(T):
    """Compute size of binary tree"""
    if T == None:
        return(0)
    else:
        return(1 + size(T.left) + size(T.right))


def depth(T):
    """Compute depth of binary tree"""
    if T == None:
        return(-1)
    else:
        return(1 + max(depth(T.left), depth(T.right)))


def pathLengths(T, h=0):
    """Total paths lengths of tree"""
    if T == None:
        return(0)
    else:
        return(h + pathLengths(T.left, h + 1) + pathLengths(T.right, h + 1))


def averageDepth_bad(T):
    """Average depth of tree nodes """
    if T == None:
        return(0)
    else:
        return(pathLengths(T)/size(T))  # Takes two traversals of T


def pathLengths_enhanced(T, h=0):
    """Total paths lengths of tree and size"""
    if T == None:
        return(0, 0)
    else:
        path_left = pathLengths_enhanced(T.left, h + 1)
        path_right = pathLengths_enhanced(T.right, h + 1)

        path = h + path_left[0] + path_right[0]
        size = 1 + path_left[1] + path_right[1]

        return(path, size)


def averageDepth(T):
    """Average depth of tree nodes"""
    path, size = pathLengths_enhanced(T)

    if size == 0:
        return(0)
    else:
        return(path/size)


def __externalPathLengths(T, h=0, n=0):
    if T == None:
        return(0, 0)
    elif T.left == None and T.right == None:   # check if we are a leaf
        return(h, 1)
    else:
        extpath_left = __externalPathLengths(T.left, h+1)
        extpath_right = __externalPathLengths(T.right, h+1)

        return(extpath_left[0] + extpath_right[0],
               extpath_left[1] + extpath_right[1])


def externalPathLengths(T):
    """Total external paths lengths of a tree"""
    return(__externalPathLengths(T)[0])


def averageExtPathLengths(T):
    """Average external paths lengths of a tree"""
    if T == None:
        return(0)
    else:
        ext_paths, nb_leaves = __externalPathLengths(T)
        return(ext_paths/nb_leaves)

    ##################################################
    ##################################################
    ##################################################

# -------------------------From Implementation to Abstract---------------------


def __DfsPrint(T):
    s = ""

    if T == None:
        s += "_"
    else:
        s += "<{},".format(T.key)
        s += "{},".format(__DfsPrint(T.left))
        s += "{}>".format(__DfsPrint(T.right))

    return(s)


def DfsPrint(T):
    """Prints abstract form of tree"""
    print(__DfsPrint(T))


    #################################################
    #################################################
    #################################################


strB = "RSE##Q##FG##H##"

def __deSerializeTree(serial, i):
    i += 1
    key = serial[i]
    if key == "#":
        return None, i
    else:
        node = bintree.BinTree(key, None, None)
        node.left, i = __deSerializeTree(serial, i)
        node.right, i = __deSerializeTree(serial, i)
        return node, i


def deSerializeTree(serial):
    if serial == "#":
        return None
    else:
        i = -1
        tree, _ = __deSerializeTree(serial, i)
    return tree


def __serialize(T, serial):

    if not T:
        serial.append("#")
    else:
        serial.append(T.key)
        __serialize(T.left, serial)
        __serialize(T.right, serial)


def serializeTree(T):
    """Writes tree serially as a list of keys, returns list."""
    if T is None:
        return "#"
    else:
        serial = []
        __serialize(T, serial)
    return(serial)

#######################################################
################HOW TO PRINT TREES#####################
#######################################################


def __print_tree (B,string):
    if B == None:
        print (string + "#")
    else:
        res = string + B.key
        print (res)
        string += "   | "
        __print_tree(B.right, string)
        __print_tree(B.left, string)

def print_tree (B):
    if B == None:
        return None
    else:
        res = "| "
        __print_tree(B,res)

def search (B, x):
    if B == None:
        return None
    else :
        if x == B.key:
            return B
        else:
            res = search(B.left, x)
            if res != None:
                return res
            else:
                return search(B.right, x)

def __occurence (B, x, path):
    if B == None:
        return None
    else :
        if x == B.key:
            return path
        else:
            res = __occurence(B.left, x,path + "0")
            if res != None:
                return res
            else:
                return __occurence(B.right, x,path + "1")

def occurence (B,x):
    res = __occurence(B,x,"")
    if res == "":
        return chr(949)
    else :
        return res


def width (B):
    w_max = 0
    q =queue.Queue()
    q.enqueue(B)
    q.enqueue(None)
    while not q.isempty():
        w = 0
        B = q.dequeue()
        fun.printqu
        if B == None and not q.isempty():
            w = fun.len_queue(q)
            q.enqueue(None)
            w_max = max (w_max,w)
        else:
            q.enqueue(B.left)
            q.enqueue(B.right)
    return w_max

def addparent (B, P = None):
    if B == None :
        return None
    else :
        C = bintree.BinTree((B.key, P),None,None)
        C.left = addparent(B.left,C)
        C.right = addparent(B.right,C)
        return C

def __copy (B):
    C = bintree.Bintree_Parent(B.key,None,None,None)
    if B.left != None:
        C.left = __copy(B.left)
        C.left.parent = C
    if B.right != None:
        C.left.parent =C
        C.right = __copy(B.right)
    return C

def copy__parent (B):
    if B == None:
        return None
    else:
        return __copy(B)

def IsDegenerate (B):
    if B == None:
        return True
    else:
        if not(((B.left != None) and (B.right == None)) or ((B.left == None) and (B.right != None))):
            return False
        else:
            return (IsDegenerate(B.left) and IsDegenerate(B.right))

def IsPerfect (B): #complet in french
    q = queue.Queue()
    q.enqueue(B)
    q.enqueue(None)
    length = 0
    max_length = 1
    isperfect = True
    while not q.isempty() and isperfect:
        B = q.dequeue()
        if B == None:
            if not q.isempty():
                q.enqueue(None)
                isperfect = (length == 2*max_length)
            max_length = length
            length = 0
        else:
            if B.left != None:
                length += 1
                q.enqueue(B.left)
            if B.right != None:
                length += 1
                q.enqueue(B.right)
    return isperfect

def __IsPerfect_upward (B):
    if B.right == B.left:
        return (True,0)
    else:
        if B.left == None or B.right == None:
            return (False,666)
        else:
            (okeyl,hieghtl) = __IsPerfect_upward(B.left)
            if not (okeyl):
                return(false,666)
            else:
                (okeyr,hieghtr) = __IsPerfect_upward(B.right)
            return (okeyr and okeyl and (hieghtr == hieghtl),hieghtl +1)


def IsPerfect_upward (B):
    if B == None:
        return True
    else:
        (ok,height) = __IsPerfect_upward(B)
    return ok

def equal (B1,B2):
    if B1 == None and B2 == None :
        return True
    else:
        if B1.key != B2.key :
            return False
        else:
            left = equal(B1.left,B2.left)
            if left :
                return equal(B1.right,B2.right)
            else:
                return False


def __node(B,cpt,cpd):
    if B ==None:
        return 0
    if B.left == None and B.right == None:
        return (cpt,cpd +1)
    else:
        cpt += 1
        __node(B.left,cpt,cpd)
        __node(B.right,cpt,cpd)
    return (cpt,cpd)


def node (B):
    if B == None :
        return False
    else:
        return __node(B,0,0)

def __affichemoi(B,res):
    if B.left == None and B.right == None:
        res += B.key
        return res
    else:
        res += "("
        res = __affichemoi(B.left,res)
        res += B.key
        res = __affichemoi(B.right,res)
        res += ")"
    return res

def affichemoi (B):
    if B == None :
        return False
    else:
        return __affichemoi(B,"")






tree_test_string = "Q#B#C#T#BN##E##"
T = deSerializeTree(tree_test_string)
print (serializeTree(T))
print_tree(T)
print(" ")
DfsPrint(T)
#print(IsDegenerate(T))
#print(IsPerfect(T))
#print(IsPerfect_upward(T))

tree_test_string = "VDI##G##SE##F##"
C = deSerializeTree(tree_test_string)
print (serializeTree(C))
print_tree(C)
print(" ")
DfsPrint(C)
#print("Dege")
#print(IsDegenerate(C))
#print("Comp")
#print(IsPerfect(C))
#print(IsPerfect_upward(C))
#print (width(C))


tree_test_string = "GFK#FD##R#FD##DG###VVS##DGGH########"
N = deSerializeTree(tree_test_string)
print (serializeTree(N))
print_tree(N)
print(" ")
DfsPrint(N)

#print(width(T))
#print(" ")
#B = deSerializeTree(strB)
#print (serializeTree(B))
#print_tree(B)
#DfsPrint(B)
#print(width(B))
#F = occurence(T,'E')
#print(F)
#G = occurence(T,'U')
#print (G)

#print ("T / C")
#print (equal(T,C))
#print ("C / B")
#print (equal(C,C))
#print ("T / N")
#print (equal(T,N))
#print ("N / C")
#print (equal(N,C))
#print ("N / N")
#print (equal(N,N))
#print (node(C))



tree_test_string = "+*-A##B##C##/*D##E##+F##G##"
H = deSerializeTree(tree_test_string)
print (serializeTree(H))
print_tree(H)
print(" ")
DfsPrint(H)
print(affichemoi(H))
