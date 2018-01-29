#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 09:30:00 2017

@author: nathalie
"""

import bintree

# BST -> list
def __bst2list(B, L):
    if B != None:
        __bst2list(B.left, L)
        L.append(B.key)
        __bst2list(B.right, L)


def bst2list(B):
    L = []
    __bst2list(B, L)
    return L


# list -> BST: warning, works only with strictly increasing lists!

def __list2bst(L, left, right):
    if left == right:
        return None
    else:
        mid = left +  (right - left) // 2
        B = bintree.BinTree(L[mid], None, None)
        B.left = __list2bst(L, left, mid)
        B.right = __list2bst(L, mid+1, right)
        return B


def list2bst(L):
    return __list2bst(L, 0, len(L))

# test

def __testbst(B, inf, sup):
    if B == None:
        return True
    else:
        if B.key > inf and B.key <= sup:
            return __testbst(B.left, inf, B.key) \
                    and __testbst(B.right, B.key, sup)
        else:
            return False


def testbst(B):
    return __testbst(B, -float('inf'), float('inf'))


# search

def searchBST(B, x):
    if B == None or B.key == x:
        return B
    else:
        if x < B.key:
            return searchBST(B.left, x)
        else:
            return searchBST(B.right, x)

def searchBST_iter(B, x):
    while B != None and B.key != x:
        if x < B.key:
            B = B.left
        else:
            B = B.right
    return B


# insertions


def leaf_insert(B, x):
    if B == None:
        return bintree.BinTree(x, None, None)
    else:
        if x <= B.key:
            B.left = leaf_insert(B.left, x)
        else:
            B.right = leaf_insert(B.right, x)
        return B

def leaf_insert_iter(B, x):
    new = bintree.BinTree(x, None, None)
    P = None
    T = B
    while T != None:
        P = T
        if x <= T.key:
            T = T.left
        else:
            T = T.right

    if P == None:
        return new
    else:
        if x <= P.key:
            P.left = new
        else:
            P.right = new
        return B

# tests

def buildBST(L):
    B = None
    for e in L:
        B = leaf_insert(B, e)
    return B

def buildBST_iter(L):
    B = None
    for e in L:
        B = leaf_insert_iter(B, e)
    return B


L = [13, 20, 5, 1, 15, 10, 18, 25, 4, 21, 27, 7, 12]
F = [2, 6, 12, 13, 15, 17, 34, 47, 50,59,60,71,82,94]


"""
delete
"""

def maxBST(B):
    """
    B != None
    """
    while B.right != None:
        B = B.right
    return B.key


def del_bst(B, x):
    if B == None:
        return None
    else:
        if x == B.key:
            if B.left == None:
                return B.right
            elif B.right == None:
                return B.left
            else:
                B.key = maxBST(B.left)
                B.left = del_bst(B.left, B.key)
                return B
        else:
            if x < B.key:
                B.left = del_bst(B.left, x)
            else:
                B.right = del_bst(B.right, x)
            return B


def del_max_bst(B):
    """
    B != None
    """
    if B.right == None:
        return (B.left, B.key)
    else:
        (B.right, m) = del_max_bst(B.right)
        return (B, m)


def del_bst_opti(B, x):
    if B == None:
        return None
    else:
        if x == B.key:
            if B.left == None:
                return B.right
            elif B.right == None:
                return B.left
            else:
                (B.left, B.key) = del_max_bst(B.left)
                return B
        else:
            if x < B.key:
                B.left = del_bst_opti(B.left, x)
            else:
                B.right = del_bst_opti(B.right, x)
            return B


"""
root insertion
"""

def cut(B, x):
    if B == None:
        return (None, None)
    else:
        if B.key <= x:
            G = B
            (G.right , D) = cut(B.right, x)
        else:
            D = B
            (G, D.left) = cut(B.left, x)
        return (G, D)


def root_insertion(B, x):
    (G, D) = cut(B, x)
    return bintree.BinTree(x, G, D)

B = list2bst(L)
bintree.print_tree(B)
print (testbst(B))
C = list2bst(F)
bintree.print_tree(C)
print (testbst(C))
