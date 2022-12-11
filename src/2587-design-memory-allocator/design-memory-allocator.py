# You are given an integer n representing the size of a 0-indexed memory array. All memory units are initially free.
#
# You have a memory allocator with the following functionalities:
#
#
# 	Allocate a block of size consecutive free memory units and assign it the id mID.
# 	Free all memory units with the given id mID.
#
#
# Note that:
#
#
# 	Multiple blocks can be allocated to the same mID.
# 	You should free all the memory units with mID, even if they were allocated in different blocks.
#
#
# Implement the Allocator class:
#
#
# 	Allocator(int n) Initializes an Allocator object with a memory array of size n.
# 	int allocate(int size, int mID) Find the leftmost block of size consecutive free memory units and allocate it with the id mID. Return the block's first index. If such a block does not exist, return -1.
# 	int free(int mID) Free all memory units with the id mID. Return the number of memory units you have freed.
#
#
#  
# Example 1:
#
#
# Input
# ["Allocator", "allocate", "allocate", "allocate", "free", "allocate", "allocate", "allocate", "free", "allocate", "free"]
# [[10], [1, 1], [1, 2], [1, 3], [2], [3, 4], [1, 1], [1, 1], [1], [10, 2], [7]]
# Output
# [null, 0, 1, 2, 1, 3, 1, 6, 3, -1, 0]
#
# Explanation
# Allocator loc = new Allocator(10); // Initialize a memory array of size 10. All memory units are initially free.
# loc.allocate(1, 1); // The leftmost block's first index is 0. The memory array becomes [1,_,_,_,_,_,_,_,_,_]. We return 0.
# loc.allocate(1, 2); // The leftmost block's first index is 1. The memory array becomes [1,2,_,_,_,_,_,_,_,_]. We return 1.
# loc.allocate(1, 3); // The leftmost block's first index is 2. The memory array becomes [1,2,3,_,_,_,_,_,_,_]. We return 2.
# loc.free(2); // Free all memory units with mID 2. The memory array becomes [1,_, 3,_,_,_,_,_,_,_]. We return 1 since there is only 1 unit with mID 2.
# loc.allocate(3, 4); // The leftmost block's first index is 3. The memory array becomes [1,_,3,4,4,4,_,_,_,_]. We return 3.
# loc.allocate(1, 1); // The leftmost block's first index is 1. The memory array becomes [1,1,3,4,4,4,_,_,_,_]. We return 1.
# loc.allocate(1, 1); // The leftmost block's first index is 6. The memory array becomes [1,1,3,4,4,4,1,_,_,_]. We return 6.
# loc.free(1); // Free all memory units with mID 1. The memory array becomes [_,_,3,4,4,4,_,_,_,_]. We return 3 since there are 3 units with mID 1.
# loc.allocate(10, 2); // We can not find any free block with 10 consecutive free memory units, so we return -1.
# loc.free(7); // Free all memory units with mID 7. The memory array remains the same since there is no memory unit with mID 7. We return 0.
#
#
#  
# Constraints:
#
#
# 	1 <= n, size, mID <= 1000
# 	At most 1000 calls will be made to allocate and free.
#
#


# class Allocator:

#     def __init__(self, n: int):
#         self._m = [[0, n, -1]]
#         self._free = n
#         self.n = n

#     def allocate(self, size: int, mID: int) -> int:
#         if size > self._free: return -1
#         idx = -1
#         for i, b in enumerate(self._m):
#             if b[2] == -1:
#                 l = b[1] - b[0]
#                 if l == size:
#                     self._m[i][2] = mID
#                     self._free -= size
#                     idx = b[0]
#                     break
#                 if l > size:
#                     idx = b[0]
#                     self._m = self._m[:i] + [[b[0], b[0] + size, mID], [b[0] + size, b[1], -1]] + self._m[i+1:]
#                     self._free -= size
#                     break
#         return idx

#     def free(self, mID: int) -> int:
#         cnt = 0
#         for i, b in enumerate(self._m):
#             if b[2] == mID:
#                 cnt += b[1] - b[0]
#                 b[2] = -1
#                 if i > 0 and self._m[i - 1][2] == -1:
#                     b[0] = self._m[i - 1][0]
#                     self._m[i - 1][1] = self._m[i - 1][0]
#                 if i < len(self._m) - 1 and self._m[i + 1][2] == -1:
#                     b[1] = self._m[i + 1][1]
#                     self._m[i + 1][0] = self._m[i + 1][1]
#         self._free += cnt
#         return cnt

class Allocator:

    def __init__(self, n: int):
        self._m = [-1] * n
        self._free = n
        self.n = n

    def allocate(self, size: int, mID: int) -> int:
        if size > self._free: return -1
        l, r = 0, 0
        while r < self.n and r - l < size:
            if self._m[r] == -1:
                r += 1
            else:
                l, r = r + 1, r + 1
        if r - l == size:
            for i in range(l, r):
                self._m[i] = mID
            self._free -= size
            return l
        return -1

    def free(self, mID: int) -> int:
        cnt = 0
        for i in range(self.n):
            if self._m[i] == mID:
                cnt += 1
                self._m[i] = -1
        self._free += cnt
        return cnt


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)
