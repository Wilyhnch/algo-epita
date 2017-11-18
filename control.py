import bintree
import queue
import stack
import fun
import bintd


tree_test_string = "GFK#FD##R##FD##DG###VVS##DGGH######"
N = bintd.deSerializeTree(tree_test_string)
print (bintd.serializeTree(N))
bintd.print_tree(N)
print(" ")
bintd.DfsPrint(N)

tree_test_string = "ABC##D##BD##C##"
S = bintd.deSerializeTree(tree_test_string)
print (bintd.serializeTree(S))
bintd.print_tree(S)
print(" ")
bintd.DfsPrint(S)

tree_test_string = "ABC##J##BD##C##"
B = bintd.deSerializeTree(tree_test_string)
print (bintd.serializeTree(B))
bintd.print_tree(B)
print(" ")
bintd.DfsPrint(B)

def creat_list (B,l = []):
    if B == None:
        return False
    else:
        creat_list(B.left,l)
        l.append(B.key)
        creat_list(B.right,l)
        return l
l = []
l = creat_list(N,l)
print("N =",l)
b = []
b = creat_list(S,b)
print ("S =",b)
c = []
c = creat_list(B,c)
print("C =",c)

def symetric (B):
    l = creat_list(B)
    (i,is_sym) = (0,True)
    length = len(l)
    if (length%2 == 0):
        return False
    else:
        while i< length // 2 and is_sym:
            if l[i] != l[length-1-i]:
                is_sym = False
            i+=1
        return is_sym

print ("S ",symetric(S))
print("N " ,symetric(N))
print("B ",symetric(B))
