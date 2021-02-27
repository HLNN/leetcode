# Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.
#
#  
# Example 1:
#
#
# Input: n = 3
# Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
#
#
# Example 2:
#
#
# Input: n = 1
# Output: [[1]]
#
#
#  
# Constraints:
#
#
# 	1 <= n <= 8
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
    
