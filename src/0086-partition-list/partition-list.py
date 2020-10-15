# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the two partitions.
#
# Example:
#
#
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        lt, gt = ListNode(), ListNode()
        dummy = [lt, gt]
        
        while head:
            if head.val < x:
                lt.next = head
                lt = lt.next
            else:
                gt.next = head
                gt = gt.next
            head = head.next
        
        lt.next, gt.next = dummy[1].next, None
        return dummy[0].next
    
