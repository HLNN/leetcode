# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.
#
# Example:
#
#
# Input: 3
# Output:
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#
#
#  
# Constraints:
#
#
# 	0 <= n <= 8
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if not n: return []
        @lru_cache(None)
        def gen(nodes):
            if not nodes: return [None]
            trees = []
            for i in range(len(nodes)):
                l = gen(nodes[:i])
                r = gen(nodes[i + 1:])
                for nl in l:
                    for nr in r:
                        root = TreeNode(val=int(nodes[i]))
                        root.left = nl
                        root.right = nr
                        trees.append(root)
            return trees
        
        return gen("".join([str(i) for i in range(1, n + 1)]))
    
