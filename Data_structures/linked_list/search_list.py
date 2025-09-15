node1=[10,None]
node2=[20,None]
node3=[30,None]
node4=[40,None]

node1[1]=node2
node2[1]=node3
node3[1]=node4

head=node1

def search_linkedlist(head):
  current=head
  while current is not None:
    if current==head:
      return ture
  return false
