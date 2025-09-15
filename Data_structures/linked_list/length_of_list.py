node1=[10,None]
node2=[20,None]
node3=[30,None]

node1[1]=node2
node2[1]=node3

head=node1

def lenght_linkedlist(head):
  count=0
  current=head
  while current is not None:
    count +=1
    current[0]=current[1]
  return count

print(lenght_linkedlist(head))
