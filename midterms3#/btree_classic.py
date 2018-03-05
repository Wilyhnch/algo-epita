# 2.1: min and mx

def minBTree(B):
    '''
    B is not empty
    '''
    while B.children != []:
        B = B.children[0]
    return B.keys[0]


def maxBTree(B):
    while B.children:
        B = B.children[B.nbkeys]  # B.children[-1]
    return B.keys[B.nbkeys-1]   # B.keys[-1]

# 2.2: Searching


def __binarySearchPos(L, x, left, right):
    if left >= right:
        return right
    else:
        mid = left + (right - left) // 2
        if x == L[mid]:
            return mid
        elif x < L[mid]:
            return __binarySearchPos(L, x, left, mid)
        else:
            return __binarySearchPos(L, x, mid + 1, right)

def binarySearchPos(L, x):
    """
    returns the position where x is or might be in L
    """
    return __binarySearchPos(L, x, 0, len(L))

def _searchBTree(B, x):
    i = binarySearchPos(B.keys, x)
    if i < B.nbkeys and B.keys[i] == x:
        return (B, i)
    else:
        if B.children == []:
            return (None, -1)
        else:
            return _searchBTree(B.children[i], x)


def searchBTree(B, x):
    if B == None:
        return (None, -1)
    else:
        return _searchBTree(B,x)



# 2.3 insertion

def split(B, i):
    '''
    splits the child i of B
    conditions:
    - B is a nonempty tree and its root is not a 2t-node.
    - The child i of B exists and its root is a 2t-node.
    '''
    L = B.children[i]
    R = btree.BTree()
    mid = B.degree - 1

    (L.keys, xmid, R.keys) = (L.keys[:mid], L.keys[mid], L.keys[mid+1:])

    if L.children:
        (L.children, R.children) = (L.children[:mid+1], L.children[mid+1:])

    B.keys.insert(i, xmid)
    B.children.insert(i+1, R)
