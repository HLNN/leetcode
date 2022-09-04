# Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.
#
# The length of the path between two nodes is represented by the number of edges between them.
#
#  
# Example 1:
#
#
# Input: root = [5,4,5,1,1,null,5]
# Output: 2
# Explanation: The shown image shows that the longest path of the same value (i.e. 5).
#
#
# Example 2:
#
#
# Input: root = [1,4,5,4,4,null,5]
# Output: 2
# Explanation: The shown image shows that the longest path of the same value (i.e. 4).
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree is in the range [0, 104].
# 	-1000 <= Node.val <= 1000
# 	The depth of the tree will not exceed 1000.
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node, v):
            if not node: return 0, 0

            ml, al = dfs(node.left, node.val)
            mr, ar = dfs(node.right, node.val)
            
            ans = max(al, ar) + 1
            m = max(ans, ml, mr)
            if node.left and node.right and node.left.val == node.right.val:
                m = max(m, al + ar + 1)
            return m, ans if node.val == v else 0
        
        return max(0, dfs(root, -1)[0] - 1)
    
