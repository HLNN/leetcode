# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
#
#  
# Example 1:
#
#
# Input: head = [1,1,2]
# Output: [1,2]
#
#
# Example 2:
#
#
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the list is in the range [0, 300].
# 	-100 <= Node.val <= 100
# 	The list is guaranteed to be sorted in ascending order.
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
        # dummy = ListNode(0)
        pointer = head
        while pointer and pointer.next:
            if pointer.val == pointer.next.val:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next
        return head
        
