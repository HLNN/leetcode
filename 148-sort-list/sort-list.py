# Sort a linked list in O(n log n) time using constant space complexity.
#
# Example 1:
#
#
# Input: 4->2->1->3
# Output: 1->2->3->4
#
#
# Example 2:
#
#
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None or head.next == None:
            return head;
        
        pre = ListNode(0)
        slow = fast = head;
    
        while fast != None and fast.next != None:
          pre = slow;
          slow = slow.next;
          fast = fast.next.next;
    
        pre.next = None;
    
        l1 = self.sortList(head);
        l2 = self.sortList(slow);
    
        return self.merge(l1, l2);
    
  
    def merge(self, l1, l2):
        p = dummy = ListNode(0)
        
    
        while l1 != None and l2 != None:
          if l1.val < l2.val:
            p.next = l1;
            l1 = l1.next;
          else:
            p.next = l2;
            l2 = l2.next;
          p = p.next;
        
        if l1 != None:
          p.next = l1;

        if l2 != None:
          p.next = l2;

        return dummy.next;
