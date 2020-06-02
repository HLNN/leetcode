# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
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
