class Stack():
    def __init__(self):
        self.stack = []

    def push(self, new_item):
        self.stack.append(new_item)

    def stack_pop(self):
        self.stack.pop()

    def peak(self):
        return self.stack[-1]

s1 = Stack()
s1.push(3)
s1.push(7)
s1.push(10)
print(s1.peak())
s1.append()
print(s1.peak())
