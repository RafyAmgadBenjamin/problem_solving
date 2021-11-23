from collections import deque


class MyQueue(object):
    def __init__(self):
        self.stack_a = deque()
        self.stack_b = deque()

    def peek(self):
        self.prepare_stack()
        val = self.stack_b.pop()
        self.stack_b.append(val)
        return val

    def pop(self):
        # if not self.stack_b:
        self.prepare_stack()

        self.stack_b.pop()

    def prepare_stack(self):
        if not self.stack_b:
            while self.stack_a:
                self.stack_b.append(self.stack_a.pop())

    def put(self, value):
        # while self.stack_b:
        #     self.stack_a.append(self.stack_b.pop())
        self.stack_a.append(value)


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
