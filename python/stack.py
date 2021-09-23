
class Stack:

    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if len(self.stack) < 1:
            return None
        else:
            self.stack.pop()
    
    def peek(self):
        return self.stack.pop()

    def isEmpty(self):
        return bool(len(self.stack) == 0)
    
    def size(self):
        return len(self.stack)



# Stack test
input_stack = Stack()

input_stack.push("a")
input_stack.push("b")
input_stack.push("c")

input_stack.pop()
print(input_stack.peek())
print(input_stack.isEmpty())
print(input_stack.size())
