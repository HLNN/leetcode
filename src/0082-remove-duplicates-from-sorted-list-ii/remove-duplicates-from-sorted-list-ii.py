# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
#
# Return the linked list sorted as well.
#
# Example 1:
#
#
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
#
#
# Example 2:
#
#
# Input: 1->1->1->2->3
# Output: 2->3
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        last = dummy = ListNode(0)
        while head and head.next:
            if head.val == head.next.val:
                val = head.val
                while head and head.val == val:
                    head = head.next
            else:
                last.next = head
                last = last.next
                head = head.next
        last.next = head
        return dummy.next
