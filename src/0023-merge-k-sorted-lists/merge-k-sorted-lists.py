# Given an array of linked-lists lists, each linked list is sorted in ascending order.
#
# Merge all the linked-lists into one sort linked-list and return it.
#
#  
# Example 1:
#
#
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
#
#
# Example 2:
#
#
# Input: lists = []
# Output: []
#
#
# Example 3:
#
#
# Input: lists = [[]]
# Output: []
#
#
#  
# Constraints:
#
#
# 	k == lists.length
# 	0 <= k <= 10^4
# 	0 <= lists[i].length <= 500
# 	-10^4 <= lists[i][j] <= 10^4
# 	lists[i] is sorted in ascending order.
# 	The sum of lists[i].length won't exceed 10^4.
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next
