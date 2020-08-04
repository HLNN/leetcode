# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid palindrome.
#
# Example 1:
#
#
# Input: "A man, a plan, a canal: Panama"
# Output: true
#
#
# Example 2:
#
#
# Input: "race a car"
# Output: false
#
#
#  
# Constraints:
#
#
# 	s consists only of printable ASCII characters.
#
#


class Solution:
    def isPalindrome(self, s: str) -> bool:
        def alpnum(c):
            if "a" <= c <= "z" or "A" <= c <= "Z" or c.isdigit():
                return True
            else:
                return False
            
        if not s: return True
        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            print(l, r)
            if not alpnum(s[l]): l += 1
            elif not alpnum(s[r]): r -= 1
            else:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
        return True
            
