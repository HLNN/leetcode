# Reverse a linked list from position m to n. Do it in one-pass.
#
# Note: 1 ≤ m ≤ n ≤ length of list.
#
# Example:
#
#
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head: return None
        
        dummy = cur = ListNode(next=head)
        
        for _ in range(m - 1):
            cur.next, cur, head = head, head, head.next
        
        tail, pre, head = head, head, head.next
        for _ in range(n - m):
            cur.next, head.next, pre, head = head, pre, head, head.next
        tail.next = head
        
        return dummy.next
    
