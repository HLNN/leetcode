# Given an array of integers nums, sort the array in ascending order and return it.
#
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
#
#  
# Example 1:
#
#
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
#
#
# Example 2:
#
#
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessairly unique.
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 5 * 104
# 	-5 * 104 <= nums[i] <= 5 * 104
#
#


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        return nums
    
        # quick sort with extra space
        # if len(nums) < 2: return nums
        # return self.sortArray([n for n in nums[1:] if n <= nums[0]]) + [nums[0]] + self.sortArray([n for n in nums[1:] if n > nums[0]])

        def quickSort(x, y):
            if y - x < 1: return

            # my solution
            # use random num as pivot
            # idx = randint(x, y)
            # nums[x], nums[idx] = nums[idx], nums[x]
            # curr, l, r = x, x + 1, y
            # while l <= r:
            #     if curr < l:
            #         if nums[r] <= nums[curr]:
            #             nums[r], nums[curr] = nums[curr], nums[r]
            #             curr = r
            #         r -= 1
            #     else: # curr > r
            #         if nums[l] > nums[curr]:
            #             nums[l], nums[curr] = nums[curr], nums[l]
            #             curr = l
            #         l += 1

            i = randint(x, y)
            pivot = nums[i]
            nums[i], nums[y] = nums[y], nums[i]

            i = x - 1
            for j in range(x, y):
                if nums[j] <= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]

            i += 1
            nums[i], nums[y] = nums[y], nums[i]
            
            quickSort(x, i - 1)
            quickSort(i + 1, y)

        quickSort(0, len(nums) - 1)
        return nums
    
