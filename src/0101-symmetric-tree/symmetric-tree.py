# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
#
#  
#
# But the following [1,2,2,null,3,null,3] is not:
#
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
#
#
#  
#
# Follow up: Solve it both recursively and iteratively.
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def symmetric(a, b):
            if not a and not b: return True
            
            if a and b: return a.val == b.val and symmetric(a.left, b.right) and symmetric(a.right, b.left)
            
            return False
        
        return True if not root else symmetric(root.left, root.right)
    
