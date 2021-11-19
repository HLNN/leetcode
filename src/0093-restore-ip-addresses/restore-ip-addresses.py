# A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.
#
#
# 	For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
#
#
# Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.
#
#  
# Example 1:
# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]
# Example 2:
# Input: s = "0000"
# Output: ["0.0.0.0"]
# Example 3:
# Input: s = "1111"
# Output: ["1.1.1.1"]
# Example 4:
# Input: s = "010010"
# Output: ["0.10.0.10","0.100.1.0"]
# Example 5:
# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
#
#  
# Constraints:
#
#
# 	0 <= s.length <= 20
# 	s consists of digits only.
#
#


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n < 4 or n > 12: return []
        res = []
        ans = [-1] * 4
        def bt(start, k, ans):
            if k == 4:
                if start == n:
                    res.append(ans[:])
                else:
                    return
            if start >= n or n - start > 3 * (4 - k): return
            if s[start] == "0":
                ans[k] = "0"
                return bt(start + 1, k + 1, ans)
            for i in range(1, min(3, n - start) + 1):
                if int(s[start:start + i]) < 256:
                    ans[k], tmp = s[start:start + i], ans[k]
                    bt(start + i, k + 1, ans)
                    ans[k] = tmp
        bt(0, 0, ans)
        return [".".join(ans) for ans in res]
    
