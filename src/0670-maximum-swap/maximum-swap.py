# You are given an integer num. You can swap two digits at most once to get the maximum valued number.
#
# Return the maximum valued number you can get.
#
#  
# Example 1:
#
#
# Input: num = 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
#
#
# Example 2:
#
#
# Input: num = 9973
# Output: 9973
# Explanation: No swap.
#
#
#  
# Constraints:
#
#
# 	0 <= num <= 108
#
#


class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        counter, nums = Counter(num), sorted(list(set(num)), reverse=True)
        
        l, r, idx = -1, -1, 0
        
        for i, c in enumerate(num):
            if l < 0:
                if c == nums[idx]:
                    counter[c] -= 1
                    if counter[c] == 0:
                        idx += 1
                else:
                    l = i
            else:
                if c == nums[idx]:
                    if counter[c] > 1:
                        counter[c] -= 1
                    else:
                        r = i
                        break
        
        num[l], num[r] = num[r], num[l]
        return int(''.join(num))
    
