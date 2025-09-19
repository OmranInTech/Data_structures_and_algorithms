def push(stack,item):
    stack.append(item)
    return stack

def pop(stack):
    if stack is None or len(stack) == 0:
        return None
    return stack.pop()

def peek(stack):
    if stack is None or len(stack) == 0:
        return None
    return stack[-1]

def is_empty(stack):
    return stack is None or len(stack) == 0

def size(stack):
    if stack is None:
        return 0
    return len(stack)


stack=[]
push(stack,12)
push(stack,33)
push(stack,45)
print(stack)
print(pop(stack))
print(peek(stack))
print(is_empty(stack))
print(size(stack))
