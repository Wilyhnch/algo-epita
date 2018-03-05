def __btreeValues(B, L):
    if B.children == []:
        L += B.keys

    else:

        for i in range(B.nbkeys):
            __btreeValues(B.children[i], L)
            L.append(B.keys[i])
        __btreeValues(B.children[B.nbkeys], L)

def btreeValues(B):
    L = []
    if B != None:
        __btreeValues(B, L)
    return L



def __test_Btree(B, inf, sup):
    if B.keys[0] <= inf or B.keys[B.nbkeys-1] >= sup:
        return False

    for i in range(B.nbkeys-1):
        if B.keys[i] >= B.keys[i+1]:
            return False

    if B.children:
        for i in range(B.nbkeys):
            if not __test_Btree(B.children[i], inf, B.keys[i]):
                return False
            inf = B.keys[i]
        return __test_Btree(B.children[B.nbkeys],
                            B.keys[B.nbkeys-1],
                            sup)
    else:
        return True


def __test_Btree2(B, inf, sup):
    if B.keys[0] <= inf or B.keys[B.nbkeys-1] >= sup:
        return False
    else:
        i = 0
        while i < B.nbkeys-1 and B.keys[i] < B.keys[i+1]:
            i += 1
        if i < B.nbkeys-1:
            return False
        else:
            if B.children != []:
                i = 0
                while i < B.nbkeys and __test_Btree2(B.children[i], inf, B.keys[i]):
                    inf = B.keys[i]
                    i += 1
                if i == B.nbkeys:
                    return __test_Btree2(B.children[B.nbkeys], inf, sup)
                else:
                    return False
            else:
                return True



def test_Btree_ordered(B):
    inf = float('inf')
    return (B == None) or __test_Btree(B, -inf, inf)
