# A valid number can be split up into these components (in order):
#
#
# 	A decimal number or an integer.
# 	(Optional) An 'e' or 'E', followed by an integer.
#
#
# A decimal number can be split up into these components (in order):
#
#
# 	(Optional) A sign character (either '+' or '-').
# 	One of the following formats:
#
# 		One or more digits, followed by a dot '.'.
# 		One or more digits, followed by a dot '.', followed by one or more digits.
# 		A dot '.', followed by one or more digits.
#
#
#
#
# An integer can be split up into these components (in order):
#
#
# 	(Optional) A sign character (either '+' or '-').
# 	One or more digits.
#
#
# For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].
#
# Given a string s, return true if s is a valid number.
#
#  
# Example 1:
#
#
# Input: s = "0"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "e"
# Output: false
#
#
# Example 3:
#
#
# Input: s = "."
# Output: false
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 20
# 	s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.
#
#


class Solution:
    def isNumber(self, s: str) -> bool:
        state = [
            # state 0: None
            {},
            # state 1: Leading blank
            {"blank": 1, "sign": 2, "digit": 3, ".": 4},
            # state 2: Sign
            {"digit": 3, ".": 4},
            # state 3: Digit
            {"digit": 3, ".": 5, "e": 6, "blank": 9},
            # state 4: Dot
            {"digit": 5},
            # state 5: After dot
            {"digit": 5, "e": 6, "blank": 9},
            # state 6: E
            {"sign": 7, "digit": 8},
            # state 7: Sign after e
            {"digit": 8},
            # state 8: Digit after e
            {"digit": 8, "blank": 9},
            # state 9: Following blank
            {"blank": 9},
            
        ]
        
        curState = 1
        
        for c in s:
            if "0" <= c <= "9":
                c = "digit"
            elif c in ["+", "-"]:
                c = "sign"
            elif c == " ":
                c = "blank"
            if c not in state[curState]:
                return False
            curState = state[curState][c]
        
        return True if curState in [3, 5, 8, 9] else False
    
