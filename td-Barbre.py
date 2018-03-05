"""
arbre general de recherche

->list de key en ordre croissant
               k-noeud = k-1 key et k-fils

==> B-arbre = -> arbre general de recherche
              -> de degre d si : d <= k <= 2*d (sauf pour la racine 1 <= k <= d)
              -> TOUTE les feuilles au meme niveau
"""

class B_tree:
    def __init__(self,keys=None,childrens=None):
        self.keys = keys
        self.childrens = childrens
        if keys != None:
            self.nbkeys = len(keys)
        else:
            self.nbkeys = 0



###################################################
###################################################
###################################################
###################################################


def __btree2list(G,l):
    if B.children == []:
        l += B.keys
    else:
        for i in range(B.nbkeys):
            __btree2list(B.childrens[i],l)
            l.append(B.keys[i])
        __btree2list(B.childrens[B.nbkeys],l)

def btree2list(B):
    l = []
    if B:
        __btree2list(B,l)
    return l

def __testBtree(B,inf,sup):
    if B.keys[0] <= inf or B.keys[B.nbkeys - 1] >= sup:
        return False
    for i in range (B.nbkeys - 1):
        if B.keys[i] >= B.keys[i+1]:
            return False
    if B.children != []:
        for i in range (B.nbkeys):
            if not (__testBtree(B.children[i],inf,B.keys[i])):
                return False
            inf = B.keys[i]
        return __testBtree(B.children[B.nbkeys],inf, sup)
    else:
        return True

inf = float('inf')
def test_Btree_ordered(B):
    return B == None or __testBtree(B,-inf,inf)


def __binarysearchPos(L, x, left, right):
    if right <= left:
        return right

def binarysearchPos(L,x):
    return __binarysearchPos(L, x, 0, len(L))

def __searchBtree(B,x):
    i = binarysearchPos(B.keys,x)
    if i <B.nbkeys and B.keys[i] == x:
        return (B,i)
    elif B.chilren == []:
        return (None,-1)
    else:
        return __searchBtree(B.children[i],x)


def searchBtree(B,x):
    if B == None:
        return None
    else:
        return __searchBtree(B,x)
