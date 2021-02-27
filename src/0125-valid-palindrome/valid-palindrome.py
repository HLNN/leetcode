# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
#  
# Example 1:
#
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
#
# Example 2:
#
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 2 * 105
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
            
