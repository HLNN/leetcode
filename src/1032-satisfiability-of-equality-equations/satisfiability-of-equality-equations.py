# You are given an array of strings equations that represent relationships between variables where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.
#
# Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.
#
#  
# Example 1:
#
#
# Input: equations = ["a==b","b!=a"]
# Output: false
# Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
# There is no way to assign the variables to satisfy both equations.
#
#
# Example 2:
#
#
# Input: equations = ["b==a","a==b"]
# Output: true
# Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
#
#
# Example 3:
#
#
# Input: equations = ["a==b","b==c","a==c"]
# Output: true
#
#
# Example 4:
#
#
# Input: equations = ["a==b","b!=c","c==a"]
# Output: false
#
#
# Example 5:
#
#
# Input: equations = ["c==c","b==d","x!=z"]
# Output: true
#
#
#  
# Constraints:
#
#
# 	1 <= equations.length <= 500
# 	equations[i].length == 4
# 	equations[i][0] is a lowercase letter.
# 	equations[i][1] is either '=' or '!'.
# 	equations[i][2] is '='.
# 	equations[i][3] is a lowercase letter.
#
#


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UF()
        for e in equations:
            if e[1] == '=':
                uf.union(e[0], e[3])
        for e in equations:
            if e[1] == '!' and uf.connected(e[0], e[3]):
                return False
        return True


class UF:
    def __init__(self):
        self.count = 0
        self.parent, self.size = {}, {}

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ: return

        if self.size[rootP] > self.size[rootQ]:
            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
        else:
            self.parent[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]
        self.count -= 1
    
    def connected(self, p, q):
        return self.find(p) == self.find(q)
    
    def find(self, x):
        if x not in self.parent:
            return self.new(x)
        while self.parent[x] != x:
            # Compress
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def new(self, x):
        self.count += 1
        self.parent[x] = x
        self.size[x] = 1
        return x
    
