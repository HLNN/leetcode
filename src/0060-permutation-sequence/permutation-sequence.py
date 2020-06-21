# The set [1,2,3,...,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
#
#
# 	"123"
# 	"132"
# 	"213"
# 	"231"
# 	"312"
# 	"321"
#
#
# Given n and k, return the kth permutation sequence.
#
# Note:
#
#
# 	Given n will be between 1 and 9 inclusive.
# 	Given k will be between 1 and n! inclusive.
#
#
# Example 1:
#
#
# Input: n = 3, k = 3
# Output: "213"
#
#
# Example 2:
#
#
# Input: n = 4, k = 9
# Output: "2314"
#
#


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        if n < 3:
            if n == 1: 
                return "1"
            elif k == 1:
                return "21"
            else:
                return "12"
        p = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        res = ""
        used = [False] * n
        for i in range(n - 2):
            x, k = divmod(k, p[n - 2 - i])
            for j in range(n):
                if not used[j]:
                    if x:
                        x -= 1
                        continue
                    res += str(j + 1)
                    used[j] = True
                    break
        a, b = 0, 0
        for i in range(n):
            if not used[i]:
                a = b
                b = i + 1
        if k:
            res = res + str(b) + str(a)
        else:
            res = res + str(a) + str(b)
        return res
            
