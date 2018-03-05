
"""
Measures
"""

def size(T):
    s = 1
    for i in range(T.nbchildren):
        s += size(T.children[i])
    return s

def sizeasbin(B):
    s = 1
    child = B.child
    while child != None :
        s += sizeasbin(child)
        child = child.sibling
    return s

def sizeasbin2(B):
    if B == None:
        return 0
    else:
        return 1 + sizeasbin2(B.child) \
                + sizeasbin2(B.sibling)

# height

def height(T):
    h = 0
    for child in T.children:
        h = max(h, height(child)+1)
    return h

def heightasbin(B):
    h = -1
    C = B.child
    while C != None:
        h = max(h, heightasbin(C))
        C = C.sibling
    return h + 1

def heightasbin2(B):
    if B == None:
        return -1
    else:
        return max(1 + heightasbin2(B.child), heightasbin2(B.sibling))



# External Path Length

def epl(T, h=0):
    """
    External Path Length
    """
    if T.nbchildren == 0:
        return h
    else:
        sumdepth = 0
        for child in T.children:
            sumdepth += epl(child, h+1)
        return sumdepth

def eplasbin(B, h=0):
    if B.child == None:
        sumdepth = h
    else:
        sumdepth = epl(B.child, h+1)
    if B.sibling == None:
        return sumdepth
    else:
        return sumdepth + epl(B.sibling, h)

# Profondeur moyenne externe

def __pme(T, prof=0):
    if T.nbchildren == 0:
        return (prof, 1)
    else:
        sumProf = 0
        nb = 0
        for i in range(T.nbchildren):
            (s, n) = __pme(T.children[i], prof+1)
            sumProf += s
            nb += n
        return (sumProf, nb)



def pme(T):
    (lce, nb) = __pme(T)
    return lce / nb



def __pmeBin(B, prof=0):
     """
     B: TreeAsBin
     """

     if B.child:    # if B.child != None
         (sumProf, nb) = __pmeBin(B.child, prof + 1)
     else:
         (sumProf, nb) = (prof, 1)
     if B.sibling:
        (s, n) = __pmeBin(B.sibling, prof)
        sumProf += s
        nb += n
     return (sumProf, nb)

def pmeBin(T):
    (lce, nb) = __pmeBin(T)
    return lce / nb


"""
Traversals
"""

"""
Depth First Search
"""



def dfs(T):
    print(T.key)    # preorder
    if T.nbchildren != 0:
        for i in range(T.nbchildren - 1):
            dfs(T.children[i])
            # intermediate
        dfs(T.children[T.nbchildren-1])
        # postorder

def dfsasbin(B):
    print(B.key) # preorder
    if B.child != None:
        child = B.child
        while child.sibling != None:
            dfsasbin(child)
            child = child.sibling
             # intermediate
        dfsasbin(child)
        # postorder

def dfsasbin2(B):
    # preorder
    if B.child:
        dfsasbin2(B.child)
    print(B.key, end=' ')   # postorder
    if B.sibling:
        dfsasbin2(B.sibling)


"""
Breadth First Search
"""

def bfs(T):
    q = queue.Queue()
    q.enqueue(T)
    q.enqueue(None)
    (cur, m) = (0, 0)

    while not q.isempty():
        T = q.dequeue()
        if T == None:
            m = max(m, cur)
            cur = 0
            if not q.isempty():
                q.enqueue(None)
        else:
            cur += 1
            for child in T.children:
                q.enqueue(child)
    return m

def bfsasbin(B):
    q = queue.Queue()
    q2 = queue.Queue()
    q.enqueue(B)
    while not q.isempty():
        B = q.dequeue()
        print(B.key)
        child = B.child
        while child:
            q2.enqueue(child)
            child = child.sibling
        if q.isempty():
            print()
            (q, q2) = (q2, q)
