# Given the head of a linked list, return the list after sorting it in ascending order.
#
# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
#
#  
# Example 1:
#
#
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
#
#
# Example 2:
#
#
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
#
#
# Example 3:
#
#
# Input: head = []
# Output: []
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the list is in the range [0, 5 * 104].
# 	-105 <= Node.val <= 105
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)
    
    def getMid(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid
    
    def merge(self, head1, head2):
        dummy = tail = ListNode()
        while head1 and head2:
            if head1.val < head2.val:
                tail.next, tail, head1 = head1, head1, head1.next
            else:
                tail.next, tail, head2 = head2, head2, head2.next
        tail.next = head1 or head2
        return dummy.next
    
