
node1=[10,None]
node2=[20,None]
node3=[30,None]
node4=[40,None]
node5=[50,None]

node1[1]=node2
node2[1]=node3
node3[1]=node4
node4[1]=node5

head=node1

def reverse_linked_list(head):
    prev=None
    current=head
    while current is not None:
        next_node=current[1]
        current[1]=prev
        prev=current
        current=next_node
    return prev

head=reverse_linked_list(head)
current=head
while current is not None:
    print(current[0],end=' ')
    current=current[1]
print()
