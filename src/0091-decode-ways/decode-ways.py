# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
#
# Given a non-empty string containing only digits, determine the total number of ways to decode it.
#
# The answer is guaranteed to fit in a 32-bit integer.
#
#  
# Example 1:
#
#
# Input: s = "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
#
#
# Example 2:
#
#
# Input: s = "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
#
#
# Example 3:
#
#
# Input: s = "0"
# Output: 0
# Explanation: There is no character that is mapped to a number starting with '0'. We cannot ignore a zero when we face it while decoding. So, each '0' should be part of "10" --> 'J' or "20" --> 'T'.
#
#
# Example 4:
#
#
# Input: s = "1"
# Output: 1
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 100
# 	s contains only digits and may contain leading zero(s).
#
#


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0": return 0
        if len(s) == 1: return 1
        a, b, c = 1, 1, 0
        # dp = [0] * len(s)
        # dp[0] = dp[-1] = 1
        for i in range(1, len(s)):
            if s[i] == "0":
                if "0" < s[i-1] < "3":
                    a, b, c = b, a, b
                    # dp[i] = dp[i-2]
                else:
                    return 0
            elif s[i-1] == "1" or s[i-1] == "2" and "0" < s[i] < "7":
                a, b, c = a + b, a, b
                # dp[i] = dp[i-1] + dp[i-2]
            else:
                a, b, c = a, a, b
                # dp[i] = dp[i-1]
        return a
        # return dp[-1]
    
