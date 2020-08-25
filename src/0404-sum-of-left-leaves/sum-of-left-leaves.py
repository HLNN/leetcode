# Find the sum of all left leaves in a given binary tree.
#
# Example:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root: return 0
        def dfs(node, lr):
            if node.left or node.right:
                if node.left: dfs(node.left, 1)
                if node.right: dfs(node.right, 0)
            elif lr:
                self.res += node.val
        self.res = 0
        dfs(root, 0)
        return self.res
    
