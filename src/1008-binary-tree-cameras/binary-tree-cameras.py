# You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.
#
# Return the minimum number of cameras needed to monitor all nodes of the tree.
#
#  
# Example 1:
#
#
# Input: root = [0,0,null,0,0]
# Output: 1
# Explanation: One camera is enough to monitor all nodes if placed as shown.
#
#
# Example 2:
#
#
# Input: root = [0,0,null,0,null,0,null,null,0]
# Output: 2
# Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree is in the range [1, 1000].
# 	Node.val == 0
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # 0 as unmonitored, 1 as monitored (camera), and 2 as monitored (no camera)
            if not node: return 0, 2
            
            l, r = dfs(node.left), dfs(node.right)
            res = l[0] + r[0]
            
            if l[1] == 0 or r[1] == 0:
                # has at least one unmoitored child
                return res + 1, 1
            elif l[1] == 1 or r[1] == 1:
                # has at least one camera child
                return res, 2
            else:
                return res, 0
        
        res, state = dfs(root)
        return res + (state == 0)
    
