import bintree
import queue
import stack



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
    """Average depth of tree nodes"""
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

def __print_tree (B,string):
    if B == None:
        return None
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







B = deSerializeTree(strB)
print (serializeTree(B))
print_tree(B)
