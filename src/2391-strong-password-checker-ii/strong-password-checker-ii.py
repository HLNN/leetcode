# A password is said to be strong if it satisfies all the following criteria:
#
#
# 	It has at least 8 characters.
# 	It contains at least one lowercase letter.
# 	It contains at least one uppercase letter.
# 	It contains at least one digit.
# 	It contains at least one special character. The special characters are the characters in the following string: "!@#$%^&*()-+".
# 	It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).
#
#
# Given a string password, return true if it is a strong password. Otherwise, return false.
#
#  
# Example 1:
#
#
# Input: password = "IloveLe3tcode!"
# Output: true
# Explanation: The password meets all the requirements. Therefore, we return true.
#
#
# Example 2:
#
#
# Input: password = "Me+You--IsMyDream"
# Output: false
# Explanation: The password does not contain a digit and also contains 2 of the same character in adjacent positions. Therefore, we return false.
#
#
# Example 3:
#
#
# Input: password = "1aB!"
# Output: false
# Explanation: The password does not meet the length requirement. Therefore, we return false.
#
#  
# Constraints:
#
#
# 	1 <= password.length <= 100
# 	password consists of letters, digits, and special characters: "!@#$%^&*()-+".
#
#


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8: return False

        lower = 'abcdefghijklmnopqrstuvwxyz'
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        digit = '1234567890'
        special = '!@#$%^&*()-+'
        has_lower = password[0] in lower
        has_upper = password[0] in upper
        has_digit = password[0] in digit
        has_special = password[0] in special

        for i in range(1, len(password)):
            if password[i] == password[i - 1]: return False

            if password[i] in lower:
                has_lower = True
            elif password[i] in upper:
                has_upper = True
            elif password[i] in digit:
                has_digit = True
            elif password[i] in special:
                has_special = True
        
        return has_lower and has_upper and has_digit and has_special
    
