import queue


class BinTree:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

class Bintree_Parent:
    def __init__(self,key,parent,left,right):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

class Bintree_Size:
    def __init__(self,key,left,right,size):
        self.key = key
        self.size = size
        self.left = left
        self.right = right


###############################################
###############################################

def depth(T):
    """Compute depth of binary tree"""
    if T == None:
        return(-1)
    else:
        return(1 + max(depth(T.left), depth(T.right)))


###############################################
###############################################
def chr_length (c):
    res = 0
    if isinstance(c,int):
        if c == 0:
            return 1
        else:
            while c != 0 :
                res += 1
                c = c // 10
    else:
        if c == None:
            return 1
        else:
         for i in c:
            res += 1
    return res



def __print_keylevel(keys,level,height):
    num_key = len(keys)
    space_front = 0
    for i in range (height + 1 - level):
        space_front += 2 ** i
    for i in range (space_front):
        print(" ",end = '')
    between_tree = False
    for i in range (num_key):
        if keys[i] != '#':
            print(keys[i],end = '')
        else:
            print(" ",end = '')
        chr_len = chr_length(keys[i])
        if i < num_key - 1:
            if not between_tree :
                for j in range ((2 ** (height + 1 - level))*2 + 1 - chr_len):
                    print (" ",end = '')
            else:
                for j in range (((2 **(height + 1 - level))*2) - 2 + 1 - chr_len):
                    print(" ", end = '')
        between_tree = not between_tree
    print()

def __print_branches (l,level,height):
    length = len(l)
    space_front = 0
    for i in range (height + 1 - level):
        space_front += 2 ** i
    space_front -= 1
    space_middle_bar = 1
    space_middle_rep = ((2 **(height + 1 - level))*2) - 2
    i,j = -1,0
    while j < 2**(height - level):
        for k in range (space_front):
            print(" ",end = '')
        for k in range (2**level):
            i += 1
            if l[i] != '#':
                print("/",end = '')
            else:
                print(" ",end = '')
            i += 1
            for g in range (space_middle_bar):
                print(" ",end = '')
            if l[i] != '#':
                print("\\", end = '')
            else:
                print(" ",end = '')
            if i < length - 1:
                if (i % 4) != 3 :
                    for w in range (space_middle_rep):
                        print (" ",end = '')
                else:
                    for w in range (space_middle_rep - 2):
                        print(" ",end = '')
        i = -1
        j += 1
        space_front -= 1
        space_middle_bar += 2
        space_middle_rep -= 2
        print()

def pretty_print_tree (B):
    height = depth(B)
    level = 0
    q = queue.Queue()
    q.enqueue(B)
    q.enqueue('@')
    l_key = []
    l_child = []
    while level <= height:
        c = q.dequeue()
        if c == '@':
            __print_keylevel(l_key,level,height)
            __print_branches(l_child,level,height)
            l_child = []
            l_key = []
            level += 1
            if not q.isempty():
                q.enqueue('@')
        else:
            if c == '#':
                l_key.append('#')
                l_child.append('#')
                l_child.append('#')
                q.enqueue('#')
                q.enqueue('#')
            else:
                l_key.append(c.key)
                if c.left == None:
                    l_child.append('#')
                    q.enqueue('#')
                else:
                    l_child.append(c.left.key)
                    q.enqueue(c.left)
                if c.right == None:
                    l_child.append('#')
                    q.enqueue('#')
                else:
                    l_child.append(c.right.key)
                    q.enqueue(c.right)

def __print_branches_small (l,level,height):
    length = len(l)
    space_front = 0
    for i in range (height + 1 - level):
        space_front += 2 ** i
    space_front = space_front // 2
    space_middle_bar = 1
    space_middle_rep = ((2 **(height + 1 - level))*2) - 2
    for i in range (space_front):
        print(" ",end ='')
    #print ("height " , height)
    #print("level ", level)
    upto = (2**(height - level))
    #print ("upto " , upto)
    goodlength = 2
    goodlentghdone = False
    for i in range (length):
        if i % 2 == 0:
            if l[i] != '#':
                if goodlength == i and i+1 < length and l[i+1] == '#':
                    goodlength += 4
                    goodlentghdone = True
                    for j in range (upto +2):
                        print("-", end = '')
                else:
                    for j in range (upto+1):
                        print("-",end = '')
            else:
                for j in range (upto):
                    print(" ",end = '')
        elif i % 2 != 0:
            if l[i-1] == '#':
                for j in range (upto + 2):
                    if l[i] != '#':
                        print ("-",end = '')
                    else:
                        print(" ",end = '')
            else:
                for j in range (upto + 1):
                    if l[i] != '#':
                        print ("-",end = '')
                    else:
                        print(" ",end = '')
            if i < length - 1:
                if goodlentghdone:
                    goodlentghdone = False
                    for j in range (upto * 2 - 3):
                        print(" ",end = '')
                else:
                    for j in range (upto * 2 - 2):
                        print (" ",end = '')


    print()





def __print_keylevel_small(keys,l,level,height):
    num_key = len(keys)
    space_front = 0
    for i in range (height + 1 - level):
        space_front += 2 ** i
    j = 0
    if num_key == 1:
        j += 1
    while j < 3:
        for i in range (space_front):
            print(" ",end = '')
        between_tree = False
        for i in range (num_key):
            if keys[i] != '#':
                if j == 0:
                    print("|",end = '')
                else:
                    if j == 2 and (l[i+i] != '#' or l[i+i+1]!= '#'):
                        print("|",end = '')
                    else:
                        if j == 1:
                            print(keys[i],end = '')
                        else:
                            print(" ",end = '')
            else:
                print(" ",end='')

            chr_len = chr_length(keys[i])
            if i < num_key - 1:
                if not between_tree :
                    if j == 1:
                        for k in range ((2 ** (height + 1 - level))*2 + 1 - chr_len):
                            print (" ",end = '')
                    else:
                        for k in range ((2 ** (height + 1 - level))*2):
                            print (" ",end = '')
                else:
                    if j == 1:
                        for k in range (((2 **(height + 1 - level))*2) - 2 + 1 - chr_len):
                            print(" ", end = '')
                    else:
                        for k in range (((2 **(height + 1 - level))*2) - 2):
                            print(" ", end = '')
                between_tree = not between_tree
        j += 1
        print()


def pretty_print_tree_small (B):
    height = depth(B)
    level = 0
    q = queue.Queue()
    q.enqueue(B)
    q.enqueue('@')
    l_key = []
    l_child = []
    while level <= height:
        c = q.dequeue()
        if c == '@':
            __print_keylevel_small(l_key,l_child,level,height)
            __print_branches_small(l_child,level,height)
            l_child = []
            l_key = []
            level += 1
            if not q.isempty():
                q.enqueue('@')
        else:
            if c == '#':
                l_key.append('#')
                l_child.append('#')
                l_child.append('#')
                q.enqueue('#')
                q.enqueue('#')
            else:
                l_key.append(c.key)
                if c.left == None:
                    l_child.append('#')
                    q.enqueue('#')
                else:
                    l_child.append(c.left.key)
                    q.enqueue(c.left)
                if c.right == None:
                    l_child.append('#')
                    q.enqueue('#')
                else:
                    l_child.append(c.right.key)
                    q.enqueue(c.right)

def print_tree (B):
    if depth(B) < 5:
        pretty_print_tree(B)
    else:
        pretty_print_tree_small(B)


###############################################
###############################################
