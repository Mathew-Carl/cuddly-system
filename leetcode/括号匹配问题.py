class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):#进栈
        self.stack.append(element)

    def pop(self):#出栈
        return self.stack.pop()

    def get_pop(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

def brace_match(s):
    match = {'}':'{', ']':'[', ')':'('}#字典匹配
    stack = Stack()#实例化
    for ch in s:#遍历
        if ch in {'(', '[', '{'}:
            stack.push(ch)
        else: #ch in { }]) }
            if stack.is_empty():
                return False
            elif stack.get_pop() == match[ch]:
                stack.pop()
            else: #stack.get_pop() != match[ch]
                return False
    if stack.is_empty():
        return True
    else:
        return False
    
print(brace_match("[({})]"))