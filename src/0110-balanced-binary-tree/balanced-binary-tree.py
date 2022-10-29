# Given a binary tree, determine if it is height-balanced.
#
#  
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: true
#
#
# Example 2:
#
#
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
#
#
# Example 3:
#
#
# Input: root = []
# Output: true
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree is in the range [0, 5000].
# 	-104 <= Node.val <= 104
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(node):
            if not node: return True, 0
            
            l = dfs(node.left)
            if not l[0]: return False, 0
            r = dfs(node.right)
            if not r[0]: return False, 0
            
            if abs(l[1] - r[1]) <= 1: return True, max(l[1], r[1]) + 1
            
            return False, 0
        
        return dfs(root)[0]
    
