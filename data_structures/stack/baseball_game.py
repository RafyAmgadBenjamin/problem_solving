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

    def sum(self):
        total = 0
        while self.top.next != None:
            total += self.top.data
            self.top = self.top.next
        total += self.top.data
        return total

    def top(self):
        print(self.top.data)

    def pop(self):
        self.top = self.top.next

    def push_prev_sum(self):
        self.push(self.top.data + self.top.next.data)

    def push_prev_double(self):
        self.push(self.top.data * 2)


class Solution:
    def calPoints(self, ops) -> int:
        s = Stack()
        for item in ops:
            if item == "+":
                s.push_prev_sum()
            elif item == "D":
                s.push_prev_double()
            elif item == "C":
                s.pop()
            else:
                s.push(int(item))
        return s.sum()


if __name__ == "__main__":
    s = Solution()
    print(s.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))

