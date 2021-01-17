# Enter your code here. Read input from STDIN. Print output to STDOUT


class Node:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    # Issue in insert
    def insert_node(self, data):
        if not self.top:
            t = Node(data)
            self.top = t
        else:
            t = Node(max(data, self.top.data))
            t.next = self.top
            self.top = t

    def print(self):
        while self.top.next != None:
            print(self.top.data)
            self.top = self.top.next
        print(self.top.data)

    def print_max(self):
        print(self.top.data)

    def delete(self):
        self.top = self.top.next


if __name__ == "__main__":
    operations = int(input())
    s = Stack()
    for _ in range(operations):
        operation = input().split()
        if operation[0] == "1":
            value = int(operation[1])
            s.insert_node(value)
        elif operation[0] == "2":
            # delete
            s.delete()
        else:
            # print
            s.print_max()

# 68
# 1 1
# 1 44
# 3
# 3
# 2
# 3
# 3
# 1 3
# 1 37
# 2
# 3
# 1 29
# 3
# 1 73
# 1 51
# 3
# 3
# 3
# 1 70
# 3
# 1 8
# 2
# 1 49
# 1 56
# 1 81
# 2
# 1 59
# 1 44
# 2
# 3
# 3
# 2
# 3
# 3
# 1 4
# 3
# 1 89
# 2
# 1 37
# 1 50
# 1 64
# 2
# 1 49
# 1 35
# 1 85
# 3
# 1 41
# 2
# 3
# 3
# 1 86
# 3
# 1 60
# 1 8
# 3
# 1 100
# 3
# 1 83
# 3
# 1 47
# 2
# 1 78
# 2
# 1 55
# 1 97
# 2
# 3
# 1 40
