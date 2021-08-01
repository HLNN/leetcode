# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
#
# You may not alter the values in the list's nodes, only nodes themselves may be changed.
#
#  
# Example 1:
#
#
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
#
#
# Example 2:
#
#
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
#
#
# Example 3:
#
#
# Input: head = [1,2,3,4,5], k = 1
# Output: [1,2,3,4,5]
#
#
# Example 4:
#
#
# Input: head = [1], k = 1
# Output: [1]
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the list is in the range sz.
# 	1 <= sz <= 5000
# 	0 <= Node.val <= 1000
# 	1 <= k <= sz
#
#
#  
# Follow-up: Can you solve the problem in O(1) extra memory space?


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1 or head == None or head.next == None:
            return head
        dummy = last = ListNode(0)
        now = head
        
        # dummy -> ... -> last -> None
        # head/now(Node0) -> Node1 -> ... -> None
        while now:
            for _ in range(k):
                if now:
                    now = now.next
                else:
                    last.next = head
                    return dummy.next
            now = head
            for _ in range(k):
                # move now to Node0
                now = now.next
                # insert head after last
                head.next = last.next
                last.next = head
                # reset head to now
                head = now
            for _ in range(k):
                last = last.next
        return dummy.next
                
