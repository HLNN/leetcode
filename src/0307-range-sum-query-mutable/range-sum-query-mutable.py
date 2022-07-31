# Given an integer array nums, handle multiple queries of the following types:
#
#
# 	Update the value of an element in nums.
# 	Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
#
#
# Implement the NumArray class:
#
#
# 	NumArray(int[] nums) Initializes the object with the integer array nums.
# 	void update(int index, int val) Updates the value of nums[index] to be val.
# 	int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
#
#
#  
# Example 1:
#
#
# Input
# ["NumArray", "sumRange", "update", "sumRange"]
# [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
# Output
# [null, 9, null, 8]
#
# Explanation
# NumArray numArray = new NumArray([1, 3, 5]);
# numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
# numArray.update(1, 2);   // nums = [1, 2, 5]
# numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 3 * 104
# 	-100 <= nums[i] <= 100
# 	0 <= index < nums.length
# 	-100 <= val <= 100
# 	0 <= left <= right < nums.length
# 	At most 3 * 104 calls will be made to update and sumRange.
#
#


class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (self.n * 2)
        
        self.tree[-self.n:] = nums
        for i in range(self.n - 1, -1, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]
        
    def update(self, index: int, val: int) -> None:
        index += self.n
        self.tree[index] = val
        
        while index > 0:
            if index % 2 == 0:
                l, r = index, index + 1
            else:
                l, r = index - 1, index
            
            self.tree[index // 2] = self.tree[l] + self.tree[r]
            index //= 2

    def sumRange(self, left: int, right: int) -> int:
        l, r = left + self.n, right + self.n
        res = 0
        
        while l <= r:
            if l % 2 == 1:
                res += self.tree[l]
                l += 1
            if r % 2 == 0:
                res += self.tree[r]
                r -= 1
            
            l, r = l // 2, r // 2
        
        return res
    
    
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
