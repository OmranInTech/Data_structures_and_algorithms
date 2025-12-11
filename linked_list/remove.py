#remove duplicates from linkedlist
node1=[10,None]
node2=[20,None]
node3=[20,None]

node1[1]=node2
node2[1]=node3
head=node1
def remove_duplicates(head):
    current=head
    while current is not None and current[1] is not None:
        if current[0]==current[1][0]:
            current[1]=current[1][1]
        else:
            current=current[1]
    return head
head=remove_duplicates(head)
current=head
while current is not None:
    print(current[0],end=' ')
    current=current[1]
print()
