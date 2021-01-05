# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
#  
# Example 1:
#
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#
#
# Example 2:
#
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
#
# Example 3:
#
#
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#
#
#  
# Constraints:
#
#
# 	The number of nodes in each linked list is in the range [1, 100].
# 	0 <= Node.val <= 9
# 	It is guaranteed that the list represents a number that does not have leading zeros.
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        carry = 0
        x = l1.val
        y = l2.val
        a = ListNode((x + y) % 10)
        pre = a
        carry = (x + y) // 10
        l1 = l1.next
        l2 = l2.next
        
        while l1 != None or l2 != None:
            if l1 != None:
                x = l1.val
            else:
                x = 0
            if l2 != None:
                y = l2.val
            else:
                y = 0
                
            l = ListNode((x + y + carry) % 10)
            carry = (x + y + carry) // 10
            pre.next = l
            pre = l
            
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
                
        if carry:
            l = ListNode(carry)
            pre.next = l
            
        return a
        
