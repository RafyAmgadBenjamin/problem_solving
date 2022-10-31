# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        temp = head 
        nodes_adds = set()
        while(temp and temp.next != None):
            if temp in nodes_adds:
                return True
            nodes_adds.add(temp)
            temp = temp.next

        return False