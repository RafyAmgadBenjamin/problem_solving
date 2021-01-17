class Node:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    # Issue in insert
    def push(self, data):
        t = Node(data)
        if not self.top:
            self.top = t
        else:
            t.next = self.top
            self.top = t

    def print(self):
        while self.top.next != None:
            print(self.top.data)
            self.top = self.top.next
        print(self.top.data)

    def top(self):
        print(self.top.data)

    def pop(self):
        self.top = self.top.next

    def first_greater(self, value):
        temp = self.top
        value_index = 999999999
        count = 0
        while temp:
            if temp.data == value:
                value_index = count
            if temp.data > value and count > value_index:
                return temp.data
            count += 1
            temp = temp.next
        return -1


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        s = Stack()
        self.append_data(nums2, s)
        result = []
        for item in nums1:
            result.append(s.first_greater(item))

        #        print("the result")
        return result

    def append_data(self, nums2, s: Stack):
        reversed_list = []
        l = len(nums2) - 1
        for index in range(len(nums2)):
            reversed_list.append(nums2[l - index])
            index += 1
        for item in reversed_list:
            s.push(item)


if __name__ == "__main__":
    sol = Solution()
    print(sol.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
