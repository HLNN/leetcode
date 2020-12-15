# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
#
# A palindrome string is a string that reads the same backward as forward.
#
#  
# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:
# Input: s = "a"
# Output: [["a"]]
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 16
# 	s contains only lowercase English letters.
#
#


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(start):
            if start >= n: res.append(currList[:])
            
            for end in range(start, n):
                if s[start] == s[end] and (end - start <= 2 or dp[start + 1][end - 1]):
                    dp[start][end] = True
                    currList.append(s[start:end + 1])
                    dfs(end + 1)
                    currList.pop()
        
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res, currList = [], []
        
        dfs(0)
        return res
    
