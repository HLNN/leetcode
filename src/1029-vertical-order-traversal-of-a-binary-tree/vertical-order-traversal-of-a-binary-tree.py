# Given the root of a binary tree, return the vertical order traversal of its nodes values.
#
# For each node at position (x, y), its left and right children respectively will be at positions (x - 1, y - 1) and (x + 1, y - 1).
#
# Running a vertical line from x = -∞ to x = +∞, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing y coordinates).
#
# If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.
#
# Return a list of non-empty reports in order of x coordinate. Every report will have a list of values of nodes.
#
#  
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
# Explanation: Without loss of generality, we can assume the root node is at position (0, 0):
# Then, the node with value 9 occurs at position (-1, -1);
# The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
# The node with value 20 occurs at position (1, -1);
# The node with value 7 occurs at position (2, -2).
#
# Example 2:
#
#
# Input: root = [1,2,3,4,5,6,7]
# Output: [[4],[2],[1,5,6],[3],[7]]
# Explanation: The node with value 5 and the node with value 6 have the same position according to the given scheme.
# However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree is in the range [1, 1000].
# 	0 <= Node.val <= 1000
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        dic = defaultdict(list)
        self.min_l, self.max_l = float("inf"), -float("inf")
        def dfs(root, lvl_h, lvl_v):
            self.min_l = min(lvl_h, self.min_l)
            self.max_l = max(lvl_h, self.max_l)
            dic[lvl_h].append((lvl_v, root.val))
            if root.left:  dfs(root.left,  lvl_h-1, lvl_v+1)
            if root.right: dfs(root.right, lvl_h+1, lvl_v+1)
        
        dfs(root, 0, 0)
        out = []
        for i in range(self.min_l, self.max_l + 1):
            out += [[j for i,j in sorted(dic[i])]]
        return out
    
