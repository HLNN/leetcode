# Given a complete binary tree, count the number of nodes.
#
# Note: 
#
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
#
# Example:
#
#
# Input: 
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6
#
# Output: 6
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def path(self, root, num):
        for n in bin(num)[3:]:
            if n == "0":
                root = root.left
            else:
                root = root.right
            if not root: return False
        return True
        
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        
        left, depth = root, 0
        while left.left:
            left, depth = left.left, depth + 1
        
        l, r = (1 << depth), (1 << (depth + 1)) - 1
        if self.path(root, r): return r
        
        while l + 1 < r:
            m = (l + r) // 2
            if self.path(root, m):
                l = m
            else:
                r = m
        return l
            
        
