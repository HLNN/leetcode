# Given the root of a complete binary tree, return the number of the nodes in the tree.
#
# According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
#
# Design an algorithm that runs in less than O(n) time complexity.
#
#  
# Example 1:
#
#
# Input: root = [1,2,3,4,5,6]
# Output: 6
#
#
# Example 2:
#
#
# Input: root = []
# Output: 0
#
#
# Example 3:
#
#
# Input: root = [1]
# Output: 1
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree is in the range [0, 5 * 104].
# 	0 <= Node.val <= 5 * 104
# 	The tree is guaranteed to be complete.
#
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
            
        
