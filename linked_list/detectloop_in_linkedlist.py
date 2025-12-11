
#detect loop in linkedlist
node1=[10,None]
node2=[20,None]
node3=[30,None]

node1[1]=node2
node2[1]=node3
node3[1]=node1  #creates a loop


head=node1
def detect_loop(head):
    slow=head
    fast=head
    while fast is not None and fast[1] is not None:
        slow=slow[1]
        fast=fast[1][1]
        if slow==fast:
            return True
    return False

print(detect_loop(head))  #True
