
node1=[10,None]
node2=[20,None]
node3=[30,None]

node1[1]=node2
node2[1]=node3
head=node1

def middle(head):
    slow=head
    fast=head
    while fast is not None and fast[1] is not None:
        slow=slow[1]
        fast=fast[1][1]
    return slow[0]

print(middle(head))  #20
