# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given the below binary tree and sum = 22,
#
#
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
#
#
# Return:
#
#
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def dfs(root, s, ans):
            if not root: return
            if not root.left and not root.right:
                if s == root.val: self.res.append(ans + [root.val])
            
            ans.append(root.val)
            dfs(root.left, s - root.val, ans)
            dfs(root.right, s - root.val, ans)
            ans.pop()
        
        self.res = []
        dfs(root, sum, [])
        return self.res
    
