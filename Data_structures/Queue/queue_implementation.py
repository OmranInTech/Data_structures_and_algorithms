
queue=[]
def enqueue(item):
    queue.append(item)
    print('enqueueed an item :' ,{item})
def dequeue():
    return queue.pop(0)
def peek():
    return queue[0]
enqueue(12)
enqueue(14)
enqueue(66)
dequeue()
print(queue)
print('now : prenting peek')
print(peek())
