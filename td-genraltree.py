import generaltree
import queue

##############################
# ARBRE GENERAUX - TD ALGO 1 #
##############################
#         CLASSES            #
##############################

class TreeAsBin:
    """
    Simple class for (General) Trees
    represented as Binary Trees (first child - right sibling)
    """

    def __init__(self, key, child=None, sibling=None):
        """
        Init Tree
        """
        self.key = key
        self.child = child
        self.sibling = sibling


class Tree:
    """
    Simple class for (General) Trees
    represented as a Tree with a List of children
    """
    def __init__(self, key, children = None):
        """
        Init Tree
        """
        self.key = key
        if children is None:
            self.children = []
            self.nbrchildren = 0
        else:
            self.children = children
            self.nbrchildren = len(children)



##############################
#           EXO              #
##############################


def size(T):
    s = 1
    for i in range (T.nbrchildren):
        s += size(T.children[i])
    return s

def sizeAbin(T):
    if T == None:
        return 0
    else:
        res = 1 + sizeAbin(T.child) + sizeAbin(T.sibling)
    return res

def height(T):
    h = -1
    for child in T.children:
        h = max(h,heigh(children))
    return h + 1


def heightAsbin(T):
    h = -1
    C = T.child
    while C != None:
        h = max(h,heightAsbin(C))
        C = C.sibling
    return h + 1


def lce(T , prof=0):
    if T.nbrchildren == 0:
        return (prof,1)
    else:
        (prof_total , nbr_total) = (0,0)
        for child in T.children:
            (prof_current,nbr) = lce(child,prof +1)
            prof_total += prof_current
            nbr_total += nbr
        return (prof_total,nbr_total)

def pme(T):
    (prof , leaf) = lce(T)
    return (prof / leaf)

def lce_asbin(T, prof = 0):
    if T.child == None:
        return (prof,1)
    else:
        prof_total , nbr_total = 0,0
        C = T.child
        while C != None:
            curent_prof , nbr = lce_asbin(C,prof + 1)
            prof_total += curent_prof
            nbr_total += nbr
            C = C.sibling
        return (prof_total,nbr_total)

def pme_asbin(T):
    prof , leaf = lce_asbin(T)
    return (prof / leaf)

def __parcour(T,l_prefix,l_suffix):
    l_prefix.append(T.key)
    for child in T.children:
        __parcour(child,l_prefix,l_suffix)
        l_suffix.append(child.key)
    return (l_prefix,l_suffix)

def parcour(T):
    l_prefix = []
    l_suffix = []
    l_prefix , l_suffix = __parcour(T,l_prefix,l_suffix)
    print("prefix ", l_prefix)
    print("suffix ", l_suffix)


def __parcour_asbin(T,l_prefix,l_suffix):
    l_prefix.append(T.key)
    C = T.child
    while C != None:
        __parcour_asbin(C,l_prefix,l_suffix)
        C = C.sibling
    l_suffix.append(T.key)
    return (l_prefix,l_suffix)

def parcour_asbin(T):
    l_prefix = []
    l_suffix = []
    l_prefix , l_suffix = __parcour_asbin(T,l_prefix,l_suffix)
    print("prefix asbin ", l_prefix)
    print("suffix asbin ", l_suffix)


def Bfs(T):
    l_bfs = []
    q = queue.Queue()
    q.enqueue(T)
    q.enqueue(None)
    while not(q.isempty()):
        c = q.dequeue()
        if c == None:
            if not(q.isempty()):
                q.enqueue(None)
                l_bfs.append("next level")
        else:
            l_bfs.append(c.key)
            for child in c.children:
                q.enqueue(child)
    print("Bfs ",l_bfs)

def Bfs_asbin(T):
    l_bfs = []
    q = queue.Queue()
    q.enqueue(T)
    q.enqueue(None)
    while not(q.isempty()):
        c = q.dequeue()
        if c == None:
            if not(q.isempty()):
                q.enqueue(None)
                l_bfs.append("next level")
        else:
            l_bfs.append(c.key)
            child = c.child
            while child != None:
                q.enqueue(child)
                child = child.sibling
    print("Bfs asbin " , l_bfs)


def __parent(T,p):
    for child in T.children:
        p[child.key] = T.key
        __parent(child,p)

def parent(T):
    s = sizeAbin(T)
    p = [None]*s
    p[T.key] = -1
    __parent(T,p)
    return p

def dot (T,res = ""):
    for child in T.children:
        res += str(T.key) + " -- " + str(child.key) + "\n"
        res = dot(child,res)
    return res

def dot_bfs(T):
    res = ""
    l_bfs = []
    q = queue.Queue()
    q.enqueue(T)
    while not(q.isempty()):
        c = q.dequeue()
        l_bfs.append(c.key)
        for child in c.children:
            res += str(c.key) + " -- " + str(child.key) + "\n"
            q.enqueue(child)
    return res

def rep_list(T,res = ""):
    res += "("
    res += str(T.key)
    for child in T.children:
        res = rep_list(child,res)
    res += ")"
    return res

def build_from_list(res):
    curent_char = ""
    level = -1
    r_form = []
    for i in res:
        if i == "(" or i == ")":
            if curent_char != "":
                B = Tree(curent_char,[])
                r_form.append((level,B))
                curent_char = ""
            if i == ")":
                level -= 1
            else:
                level += 1
        else:
            if i != ")":
                curent_char += i
    return r_form

def build_from_r_from(L):
    B = L[0][1]
    i = 0
    for node in L:
        indice = node[0]
        tree = node[1]
        i += 1
        for j in range (i,len(L)):
            if L[j][0] == indice + 1:
                tree.children.append(L[j][1])
            else:
                if L[j][0] <= indice:
                    level_finish = True
                    break
    return B

def build_tree(res):
    list_r = build_from_list(res)
    __print_rform(list_r)
    return build_from_r_from(list_r)

def __print_rform(l):
    for i in range (len(l)):
        print("(" + str(l[i][0]) + " ; " + str(l[i][1].key) + ")", end  = '')
    print()

def __list2tree (s,i=0):
    i += 1
    key = ""
    while s[i] not in "()":
        key+= s[i]
        i += 1
    T = Tree(int(key),[])
    while s[i] == '(':
        child , i = __list2tree(s,i)
        T.children.append(child)
    i += 1
    return (T,1)

def list2tree(s):
    (T,_) = __list2tree(s)
    return T
#####################################
#           TREE TEST               #
#####################################

T1 = Tree(15,
         [Tree(3, [Tree(-6), Tree(10)]),
          Tree(8, [Tree(11, [Tree(0), Tree(4)]),
                   Tree(2),
                   Tree(5)]),
          Tree(9)])


C1 = TreeAsBin(3, TreeAsBin(-6, None, TreeAsBin(10)))
C2 = TreeAsBin(8, TreeAsBin(11, TreeAsBin(0, None, TreeAsBin(4)),
                                TreeAsBin(2, None, TreeAsBin(5))))
C3 = TreeAsBin(9)
C1.sibling = C2
C2.sibling = C3
B1 = TreeAsBin(15, C1, None)

#####################################
#              TEST                 #
#####################################

print(sizeAbin(B1))
print(heightAsbin(B1))
print(lce(T1))
print(pme(T1))
print(lce_asbin(B1))
print(pme_asbin(B1))
parcour(T1)
parcour_asbin(B1)
Bfs(T1)
Bfs_asbin(B1)
print()
print(dot_bfs(T1))
res = rep_list(T1)
print(res)
print()
#test = build_tree(res)
#print()
#print(dot_bfs(test))
print()
test = list2tree(res)
print(rep_list(test))
