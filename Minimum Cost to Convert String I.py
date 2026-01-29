# 2976. Minimum Cost to Convert String I

# Medium

# You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English letters. You are also given two 0-indexed character arrays original and changed, and an integer array cost, where cost[i] represents the cost of changing the character original[i] to the character changed[i].

# You start with the string source. In one operation, you can pick a character x from the string and change it to the character y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y.

# Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.

# Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i]. 

# Example 1:

# Input: source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]

# Output: 28

# Explanation: To convert the string "abcd" to string "acbe":
# - Change value at index 1 from 'b' to 'c' at a cost of 5.
# - Change value at index 2 from 'c' to 'e' at a cost of 1.
# - Change value at index 2 from 'e' to 'b' at a cost of 2.
# - Change value at index 3 from 'd' to 'e' at a cost of 20.
# The total cost incurred is 5 + 1 + 2 + 20 = 28.
# It can be shown that this is the minimum possible cost.

# Example 2:

# Input: source = "aaaa", target = "bbbb", original = ["a","c"], changed = ["c","b"], cost = [1,2]

# Output: 12

# Explanation: To change the character 'a' to 'b' change the character 'a' to 'c' at a cost of 1, followed by changing the character 'c' to 'b' at a cost of 2, for a total cost of 1 + 2 = 3. To change all occurrences of 'a' to 'b', a total cost of 3 * 4 = 12 is incurred.

# Example 3:

# Input: source = "abcd", target = "abce", original = ["a"], changed = ["e"], cost = [10000]

# Output: -1

# Explanation: It is impossible to convert source to target because the value at index 3 cannot be changed from 'd' to 'e'.

# Constraints:

# 1 <= source.length == target.length <= 105
# source, target consist of lowercase English letters.
# 1 <= cost.length == original.length == changed.length <= 2000
# original[i], changed[i] are lowercase English letters.
# 1 <= cost[i] <= 106


from typing import List, Tuple
import heapq

class Solution:
    def solve(self, a: int, adj: List[List[Tuple[int, int]]]) -> List[int]:
        q = [(0, a)]
        dist = [-1] * 26

        while q:
            p = heapq.heappop(q)
            for i in adj[p[1]]:
                if dist[i[0]] == -1 or p[0] + i[1] < dist[i[0]]:
                    dist[i[0]] = p[0] + i[1]
                    heapq.heappush(q, (dist[i[0]], i[0]))
        
        return dist

    def minimumCost(self, s: str, t: str, o: List[str], c: List[str], cost: List[int]) -> int:
        adj = [[] for _ in range(30)]
        n = len(o)
        for i in range(n):
            adj[ord(o[i]) - ord('a')].append((ord(c[i]) - ord('a'), cost[i]))

        m = {}
        for i in range(26):
            k = self.solve(i, adj)
            m[i] = k

        n = len(s)
        ans = 0
        for i in range(n):
            if s[i] != t[i]:
                k = m[ord(s[i]) - ord('a')][ord(t[i]) - ord('a')]
                if k == -1:
                    return -1
                ans += k

        return ans

# 2 Approach

class Solution:
    def minimumCost(self, source: str, target: str, orig: List[str], chan: List[str], cost: List[int]) -> int:
        def idx(c): return ord(c) - ord('a')
        n,tochg = idx('z') +1, Counter([(s,t) for s,t in zip(source,target) if s!=t])
        floyd   = [[0 if j==i else inf for j in range(n)] for i in range(n)]
        for o,c,s in zip(orig,chan,cost):
            floyd[idx(o)][idx(c)] = min(s, floyd[idx(o)][idx(c)])
        for k,i,j in product(range(n),range(n),range(n)):
            floyd[i][j] = min(floyd[i][j], floyd[i][k] + floyd[k][j])
        ans = sum(floyd[idx(s)][idx(t)]*tochg[(s,t)] for (s,t) in tochg.keys())
        return  ans  if  ans < 1e12  else -1