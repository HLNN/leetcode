# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
#
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#
# return its zigzag level order traversal as:
#
# [
#   [3],
#   [20,9],
#   [15,7]
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        def bfs(node, i):
            if len(res) <= i:
                res.append([node.val])
            else:
                res[i].append(node.val)
            if node.left: bfs(node.left, i+1)
            if node.right: bfs(node.right, i+1)
                
        res = []
        bfs(root, 0)
        return [level if i % 2 == 0 else level[::-1] for i, level in enumerate(res)]
    
