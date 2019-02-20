# Given a linked list, swap every two adjacent nodes and return its head.
#
# You may not modify the values in the list's nodes, only nodes itself may be changed.
#
#  
#
# Example:
#
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = head = dummy
        while 1:
            if not head.next or not head.next.next:
                return dummy.next
            else:
                slow = head.next
                fast = slow.next
                
                head.next = fast
                head = fast.next

                fast.next = slow
                slow.next = head

                head = fast = slow

