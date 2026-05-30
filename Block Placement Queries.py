# 3161. Block Placement Queries

# Hard

# There exists an infinite number line, with its origin at 0 and extending towards the positive x-axis.

# You are given a 2D array queries, which contains two types of queries:

# For a query of type 1, queries[i] = [1, x]. Build an obstacle at distance x from the origin. It is guaranteed that there is no obstacle at distance x when the query is asked.
# For a query of type 2, queries[i] = [2, x, sz]. Check if it is possible to place a block of size sz anywhere in the range [0, x] on the line, such that the block entirely lies in the range [0, x]. A block cannot be placed if it intersects with any obstacle, but it may touch it. Note that you do not actually place the block. Queries are separate.
# Return a boolean array results, where results[i] is true if you can place the block specified in the ith query of type 2, and false otherwise.

 

# Example 1:

# Input: queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]

# Output: [false,true,true]

# Explanation:



# For query 0, place an obstacle at x = 2. A block of size at most 2 can be placed before x = 3.

# Example 2:

# Input: queries = [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]

# Output: [true,true,false]

# Explanation:



# Place an obstacle at x = 7 for query 0. A block of size at most 7 can be placed before x = 7.
# Place an obstacle at x = 2 for query 2. Now, a block of size at most 5 can be placed before x = 7, and a block of size at most 2 before x = 2.
 

# Constraints:

# 1 <= queries.length <= 15 * 104
# 2 <= queries[i].length <= 3
# 1 <= queries[i][0] <= 2
# 1 <= x, sz <= min(5 * 104, 3 * queries.length)
# The input is generated such that for queries of type 1, no obstacle exists at distance x when the query is asked.
# The input is generated such that there is at least one query of type 2.

from copy import deepcopy
class Node:
    def __init__(self, flag = True, node = None):
        if flag:
            self.left = None
            self.right = None
            self.lval = 0
            self.rval = 0
            self.bestval = 0
            self.connected = True
        else:
            self.left = node.left
            self.right = node.right
            self.lval = node.lval
            self.rval = node.rval
            self.bestval = node.bestval
            self.connected = node.connected
        
def Build(l,r, arr):
    if l == r:
        return Node()
    mid = (l+r)//2
    lnode = Build(l, mid, arr)
    rnode = Build(mid+1, r, arr)
    node = Node()
    node.left = lnode
    node.right = rnode
    node.bestval = lnode.bestval + rnode.bestval+1
    node.lval = node.bestval
    node.rval = node.bestval
    return node

def update(l,r,idx, node):
    if l > r:
        return
    mid = (l+r)//2
    if l == r == idx:
        node.connected = False
        node.lval = 0
        node.rval = 0
        node.bestval = 0
        return 
    if l <= idx <= mid:
        update(l,mid, idx, node.left)
    elif mid+1 <= idx <= r:
        update(mid+1, r, idx, node.right)
    else:
        return
    lnode = node.left
    rnode = node.right
    if lnode.connected and rnode.connected:
        node.bestval = lnode.bestval + rnode.bestval+1
        node.lval = node.bestval
        node.rval = node.bestval
    elif lnode.connected:
        node.bestval = max(lnode.bestval + rnode.lval+1, rnode.bestval)
        node.lval = lnode.bestval + rnode.lval+1
        node.rval = rnode.rval
    elif rnode.connected:
        node.bestval = max(lnode.bestval, lnode.rval + rnode.bestval+1)
        node.lval = lnode.lval
        node.rval = lnode.rval + rnode.bestval+1
    else:
        node.bestval = max(lnode.bestval, rnode.bestval, lnode.rval+rnode.lval+1)
        node.lval = lnode.lval
        node.rval = rnode.rval
    node.connected = False

def query(l,r,idx, hnode):
    if l > r or idx < l:
        nnode = Node()
        nnode.bestval = -1
        nnode.lval = -1
        nnode.rval = -1
        return nnode
    mid = (l+r)//2
    if idx >= r:
        return Node(False, hnode)
    if l<=idx<=r:
        mid = (l+r)//2
        lnode = query(l, mid, idx, hnode.left)
        rnode = query(mid+1, r, idx, hnode.right)
        node = Node()
        if lnode.connected and rnode.connected:
            node.bestval = lnode.bestval + rnode.bestval+1
            node.lval = node.bestval
            node.rval = node.bestval
        elif lnode.connected:
            node.bestval = max(lnode.bestval + rnode.lval+1, rnode.bestval)
            node.lval = lnode.bestval + rnode.lval+1
            node.rval = rnode.rval
        elif rnode.connected:
            node.bestval = max(lnode.bestval, lnode.rval + rnode.bestval+1)
            node.lval = lnode.lval
            node.rval = lnode.rval + rnode.bestval+1
        else:
            node.bestval = max(lnode.bestval, rnode.bestval, lnode.rval+rnode.lval+1)
            node.lval = lnode.lval
            node.rval = rnode.rval
        node.connected = False
        return node

def ptrees(l,r,node):
    if l > r:
        return
    if l == r:
        return 
    mid = (l+r)//2
    ptrees(l, mid, node.left)
    ptrees(mid+1, r, node.right)

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        ans = []
        arr = max([i[1] for i in queries])+1
        head = Build(0, arr-1, arr)
        for curr in queries:
            if curr[0] == 1:
                x = curr[1]
                temp = head
                update(0, arr-1, x, temp)
            else:
                x,sz = curr[1], curr[2]
                temp = head
                nnode = query(0, arr-1, x, temp)
                ans.append(nnode.bestval >= sz)
            # print(head.bestval)
            
        return ans