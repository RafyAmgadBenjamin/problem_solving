# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head, val):
        if not head:
            return head
        
        dummyHead = ListNode(-1) #this is dummy node to 
        #prevent edge cases related to the beginning of the list
        dummyHead.next = head 
        tmp = dummyHead
        while (tmp and tmp.next):
            if tmp.next.val == val:
                tmp.next= tmp.next.next
            else:
                tmp = tmp.next
        return dummyHead.next

        