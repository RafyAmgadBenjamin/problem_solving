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

    def top_element(self):
        return self.top.data

    def pop(self):
        self.top = self.top.next

    # def is_there_dub(self):
    def get_data(self):
        data = ""
        if self.top:
            while self.top.next != None:
                data += self.top.data
                self.top = self.top.next
            data += self.top.data
        return data

    def is_empty(self):
        if self.top:
            return False
        return True

    # def remove_last(self):
    #     tmp_stable = self.top
    #     tmp_compr = self.top.next if self.top.next else None
    #     if tmp_compr and not tmp_compr.next:
    #         if tmp_stable.data == tmp_compr.data:
    #             self.top = None

    # def remove_adj_dub(self):
    #     is_there_dub = False
    #     tmp_stable = self.top
    #     tmp_compr = self.top.next if self.top.next else None
    #     while tmp_compr and tmp_compr.next:
    #         if tmp_compr.data == tmp_compr.next.data:
    #             tmp_compr = tmp_compr.next
    #             tmp_stable.next = tmp_compr.next
    #             tmp_compr = tmp_compr.next
    #             is_there_dub = True

    #         else:
    #             tmp_compr = tmp_compr.next
    #             tmp_stable = tmp_stable.next
    #     ## edge case
    #     # if self.top and self.top.next:
    #     #     if self.top.data == self.top.next.data:
    #     #         self.top = None

    #     return is_there_dub


class Solution:
    def removeDuplicates(self, S: str) -> str:
        s = Stack()
        for item in S:
            if not s.is_empty():
                val = s.top_element()
                if val == item:
                    s.pop()
                else:
                    s.push(item)
            else:
                s.push(item)
        # while s.remove_adj_dub():
        #     pass
        # s.remove_last()
        return s.get_data()[::-1]


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates("aaaaaaaa"))
    # print(s.removeDuplicates("abbaca"))
