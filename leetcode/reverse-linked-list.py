# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        def rev(prev, head):
            if not head:
                return prev
            tmp = head.next
            head.next = prev
            return rev(head, tmp)
        return rev(None, head)