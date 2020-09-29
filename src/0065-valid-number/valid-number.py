# Validate if a given string can be interpreted as a decimal number.
#
# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# " -90e3   " => true
# " 1e" => false
# "e3" => false
# " 6e-1" => true
# " 99e2.5 " => false
# "53.5e93" => true
# " --6 " => false
# "-+3" => false
# "95a54e53" => false
#
# Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:
#
#
# 	Numbers 0-9
# 	Exponent - "e"
# 	Positive/negative sign - "+"/"-"
# 	Decimal point - "."
#
#
# Of course, the context of these characters also matters in the input.
#
# Update (2015-02-10):
# The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.
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
    
