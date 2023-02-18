# Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.
#
#  
# Example 1:
#
#
# Input: root = [4,2,6,1,3]
# Output: 1
#
#
# Example 2:
#
#
# Input: root = [1,0,48,null,null,12,49]
# Output: 1
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree is in the range [2, 100].
# 	0 <= Node.val <= 105
#
#
#  
# Note: This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # def dfs(node):
        #     if not node:
        #         return inf, inf, -inf
        #     if not node.left and not node.right:
        #         return node.val, inf, node.val
        #     min_l, diff_l, max_l = dfs(node.left)
        #     min_r, diff_r, max_r = dfs(node.right)
        #     return min(node.val, min_l), min([diff_l, diff_r, node.val - max_l, min_r - node.val]), max(node.val, max_r)
        # return dfs(root)[1]
        
        res = inf
        last = -inf

        def dfs(node):
            if not node: return

            nonlocal res
            nonlocal last
            dfs(node.left)
            res = min(res, node.val - last)
            last = node.val
            dfs(node.right)
        
        dfs(root)
        return res
    
