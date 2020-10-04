# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.
#
#  
# Example 1:
#
#
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
#
# Example 2:
#
#
# Input: l1 = [], l2 = []
# Output: []
#
#
# Example 3:
#
#
# Input: l1 = [], l2 = [0]
# Output: [0]
#
#
#  
# Constraints:
#
#
# 	The number of nodes in both lists is in the range [0, 50].
# 	-100 <= Node.val <= 100
# 	Both l1 and l2 are sorted in non-decreasing order.
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = dummy = ListNode(0)
        
        while l1 and l2:
            if l1.val <= l2.val:
                l.next = l1
                l = l1
                l1 = l1.next
            else:
                l.next = l2
                l = l2
                l2 = l2.next
                
        if not l1:
            l.next = l2
        if not l2:
            l.next = l1
        return dummy.next
