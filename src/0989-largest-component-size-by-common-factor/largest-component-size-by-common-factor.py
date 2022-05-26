# You are given an integer array of unique positive integers nums. Consider the following graph:
#
#
# 	There are nums.length nodes, labeled nums[0] to nums[nums.length - 1],
# 	There is an undirected edge between nums[i] and nums[j] if nums[i] and nums[j] share a common factor greater than 1.
#
#
# Return the size of the largest connected component in the graph.
#
#  
# Example 1:
#
#
# Input: nums = [4,6,15,35]
# Output: 4
#
#
# Example 2:
#
#
# Input: nums = [20,50,9,63]
# Output: 2
#
#
# Example 3:
#
#
# Input: nums = [2,3,6,7,4,12,21,39]
# Output: 8
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 2 * 104
# 	1 <= nums[i] <= 105
# 	All the values of nums are unique.
#
#


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        uf = UF()
        for num in nums:
            for f in range(2, int(num ** 0.5) + 1):
                if num % f == 0:
                    uf.union(num, f)
                    uf.union(num, num // f)
        
        s = defaultdict(int)
        for num in nums:
            s[uf.find(num)] += 1
        
        return max(s.values())


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

