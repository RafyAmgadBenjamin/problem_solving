# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):
        values = []
        tmp = head 
        while tmp!= None:
            values.append(tmp.val)
            tmp = tmp.next

        return self.isPalindromArr(values)


    def isPalindromArr(self, values):
        size = len(values)-1
        for i in range(len(values)):
            if values[i] != values[size -i]:
                return False
        return True 
s = Solution()
values = [1,2,2,1]
print(s.isPalindromArr(values))