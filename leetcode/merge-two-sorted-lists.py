# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head3 = ListNode(-1)
        tmp3 = head3
        tmp1 = list1
        tmp2 = list2
        while tmp1 and tmp2 :
            if tmp1.val <= tmp2.val:
                tmp3.next = tmp1
                tmp1 = tmp1.next
            else:
                tmp3.next = tmp2
                tmp2 = tmp2.next
            tmp3 = tmp3.next
        
        while tmp1:
            tmp3.next = tmp1
            tmp1 = tmp1.next
            tmp3 = tmp3.next
        
        while tmp2:
            tmp3.next = tmp2
            tmp2 = tmp2.next
            tmp3 = tmp3.next
        
        return head3.next