node1=[10,None]
node2=[20,None]
node3=[30,None]

node1[1]=node2
node2[1]=node3

head=node1

def add_at_end(head,value):
  new_node=[value,None]
  if head is None:
    return head
  current=head
  while current is not None:
    print(current[0])
    current=current[1]
  return head
def add_at_start(head,value):
  new_node=[value ,None]
  return new_node
head=add_at_end(head,40)
head=add_at_start(head,5)
  
