#middle element of linkedlist
node1=[10,None]
node2=[20,None]
node3=[30,None]
node1[1]=node2
node2[1]=node3
head=node1
def middle(head):
    '''function for finding middle element'''
    slow=head
    fast=head
    while fast is not None and fast[1] is not None:
        slow=slow[1]
        fast=fast[1][1]
    return slow[0]
#example usage
print(middle(head))  #20
