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
expression = input("Enter a paranthesis expression: ")

for character in expression:
    if character == "(" or character == "{" or character == "[":
        s1.push(character)
    
    elif character == ")" or character == "}" or character == "]":
        
        top = s1.peak()
        
        if ( top == "(" and character != ")" ) or ( top == "{" and character != "}" ) or ( top == "[" and character != "]" ):
            print("Unbalanced paranthesis")
            break

        else:
            s1.stack_pop()

if len(s1.stack) == 0:
    print("Balanced paranthesis")

else:
    print("Unbalanced paranthesis")