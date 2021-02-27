# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
#
#  
# Example 1:
#
#
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
#
#
# Example 2:
#
#
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
#
#
#  
# Constraints:
#
#
# 	1 <= preorder.length <= 3000
# 	inorder.length == preorder.length
# 	-3000 <= preorder[i], inorder[i] <= 3000
# 	preorder and inorder consist of unique values.
# 	Each value of inorder also appears in preorder.
# 	preorder is guaranteed to be the preorder traversal of the tree.
# 	inorder is guaranteed to be the inorder traversal of the tree.
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         if not preorder: return None
#         root = TreeNode(preorder[0])
        
#         index = inorder.index(preorder[0])
#         left, right = inorder[:index], inorder[index + 1:]
        
#         if left: root.left = self.buildTree(preorder[1:len(left) + 1], left)
#         if right: root.right = self.buildTree(preorder[-len(right):], right)
        
#         return root
    
        def build(stop):
            if inorder and inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = build(root.val)
                inorder.pop()
                root.right = build(stop)
                return root
        preorder.reverse()
        inorder.reverse()
        return build(None)
    
