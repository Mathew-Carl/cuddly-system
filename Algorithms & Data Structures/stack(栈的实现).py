class Stack:
    def __init__(self):
        self = []
        
    def push(self, element):#进栈
        self.stack.append(element)
        
    def pop(self):#出栈
        return self.stack.pop()
        
    def get_pop(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

stack = Stack()