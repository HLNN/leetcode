# Given a linked list, rotate the list to the right by k places, where k is non-negative.
#
# Example 1:
#
#
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL
#
#
# Example 2:
#
#
# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head:
            dummy = ListNode(0)
            length = 0
            pointer = head
            while pointer:
                pointer = pointer.next
                length += 1

            length = length - k % length -1

            pointer = head
            for _ in range(length):
                pointer = pointer.next

            dummy.next = pointer.next
            pointer.next = None
            pointer = dummy

            while pointer.next:
                pointer = pointer.next

            pointer.next = head
            return dummy.next
        else:
            return head
