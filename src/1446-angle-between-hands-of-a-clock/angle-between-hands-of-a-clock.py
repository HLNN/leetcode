# Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.
#
# Answers within 10-5 of the actual value will be accepted as correct.
#
#  
# Example 1:
#
#
# Input: hour = 12, minutes = 30
# Output: 165
#
#
# Example 2:
#
#
# Input: hour = 3, minutes = 30
# Output: 75
#
#
# Example 3:
#
#
# Input: hour = 3, minutes = 15
# Output: 7.5
#
#
#  
# Constraints:
#
#
# 	1 <= hour <= 12
# 	0 <= minutes <= 59
#
#


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle = abs((hour % 12) * 30 - minutes * 5.5)
        return angle if angle <= 180 else 360 - angle
    
