# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
#
# Example 1:
#
#
# Input: num1 = "2", num2 = "3"
# Output: "6"
#
# Example 2:
#
#
# Input: num1 = "123", num2 = "456"
# Output: "56088"
#
#
# Note:
#
#
# 	The length of both num1 and num2 is < 110.
# 	Both num1 and num2 contain only digits 0-9.
# 	Both num1 and num2 do not contain any leading zero, except the number 0 itself.
# 	You must not use any built-in BigInteger library or convert the inputs to integer directly.
#
#


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) == 0 or len(num2) == 0 or num1 == "0" or num2 == "0":
            return "0"
        mul = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                x = int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = i + j + 1
                s = x + mul[p2]
                mul[p1] += s // 10
                mul[p2] = s % 10
        out = ""
        for i in range(len(mul)):
            if mul[i] or out:
                out += str(mul[i])
        return out
                
