# Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.
#
# The encoded string should be as compact as possible.
#
#  
# Example 1:
# Input: root = [2,1,3]
# Output: [2,1,3]
# Example 2:
# Input: root = []
# Output: []
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree is in the range [0, 104].
# 	0 <= Node.val <= 104
# 	The input tree is guaranteed to be a binary search tree.
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root: return "$"
        return ",".join([str(root.val), self.serialize(root.left), self.serialize(root.right)])

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        nodes = data.split(",")
        self.i, self.n = 0, len(nodes)
        def dfs():
            if self.i == self.n or nodes[self.i] == "$":
                self.i += 1
                return None
            node = TreeNode(int(nodes[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
