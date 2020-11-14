# Given the head of a linked list, rotate the list to the right by k places.
#
#  
# Example 1:
#
#
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
#
#
# Example 2:
#
#
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the list is in the range [0, 500].
# 	-100 <= Node.val <= 100
# 	0 <= k <= 2 * 109
#
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
