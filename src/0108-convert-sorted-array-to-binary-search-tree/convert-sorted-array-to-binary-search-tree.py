# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
#
# Example:
#
#
# Given the sorted array: [-10,-3,0,5,9],
#
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def build(start, stop):
            if start > stop: return None
            if start == stop: return TreeNode(nums[start])
            
            m = (start + stop + 1) // 2
            root = TreeNode(nums[m])
            root.left = build(start, m-1)
            root.right = build(m+1, stop)
            
            return root
    
        return build(0, len(nums) - 1)
    
