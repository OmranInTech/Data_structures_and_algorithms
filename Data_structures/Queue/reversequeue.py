queue=[10,12,14]
stack=[]
while queue:
    stack.append(queue.pop(0))

while stack:
    queue.append(stack.pop())

print(queue)