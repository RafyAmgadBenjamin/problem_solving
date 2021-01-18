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
        val = ""
        if self.top:
            val = self.top.data
            self.top = self.top.next
        return val

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


class Solution:
    def isValid(self, s: str) -> bool:
        ## Create dict with matching rules
        rules = {}
        rules["("] = ")"
        rules["["] = "]"
        rules["{"] = "}"
        st = Stack()
        closed_brackets = "}])"
        opened_brackets = "{[("
        for bracket in s:
            if bracket in opened_brackets:
                st.push(bracket)
            elif bracket in closed_brackets:
                # How to verify
                if rules.get(st.pop()) != bracket:
                    return False

        return True and st.is_empty()


if __name__ == "__main__":
    s = Solution()
    print(s.isValid("{()}"))
