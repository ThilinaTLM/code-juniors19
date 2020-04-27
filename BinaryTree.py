
"""
    Add given numbers to a binary tree.
    Author : Thilina Lakshan
    Email : thilina.18@cse.mrt.ac.lk
"""

## Tree Travels =================================================================================
def getParent(ind):
    if ind == 0:
        return None
    return ((ind + 1)//2) - 1

def getLeft(ind):
    return 2*ind + 1

def getRight(ind):
    return 2*ind + 2

"""
value of the node can be accessed by:
    -> tree[node_index]
"""

## Tree Create ===================================================================================
def addLevel(tree, current_height):
    tree.extend( ["null"]*(2**current_height) )

# add new value to the tree
## Note that "tree" (LIST), "height"(NUMBER) must have been implemented.
def addValue(val):
    global height, tree
    pos = findBinaryPos(tree, val)
    while pos >= len(tree):
        addLevel(tree, height)
    tree[pos] = val

# find relevent index for new value
def findBinaryPos(tree, val):
    n = 0 # start node (root)
    while (len(tree) > n) and tree[n] != "null":
        if val > tree[n]:
            n = getRight(n)
        else:
            n = getLeft(n)
    return n
        
## ================================================================================================

## Create empty Tree
tree = []
height = 0

values = [8, 10, 3, 14, 13, 1, 6, 4, 7] # values to add in order

# Adding values to the list
for v in values:
    addValue(v)

print(tree)

## format and print it.
## str(tree).replace("'", "") can be used to avoid single quotes and print as list


