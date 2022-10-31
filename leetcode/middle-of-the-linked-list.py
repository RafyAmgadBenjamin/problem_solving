# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        list_size = 0
        tmp = head
        nodes_add = []
        while(tmp != None):
            list_size += 1
            nodes_add.append(tmp)
            tmp = tmp.next
        if list_size == 0:
            return None
        else:
            tmp = nodes_add[int(list_size/2)]
            return tmp



        
            

        