
def add_at_end(head, value):
    new_node = [value, None]
    if head is None:
        return new_node
    current = head
    while current[1] is not None:
        current = current[1]
    current[1] = new_node 
    return head

def add_at_start(head, value):
    new_node = [value, head]  
    return new_node  

def print_list(head):
    current = head
    while current is not None:
        print(current[0], end=' -> ')
        current = current[1]
    print('None')

# Example usage
node1 = [10, None]
node2 = [20, None]
node3 = [30, None]

node1[1] = node2
node2[1] = node3

head = node1

print("Original list:")
print_list(head)

head = add_at_end(head, 40)
print("\nAfter adding 40 at end:")
print_list(head)

head = add_at_start(head, 5)
print("\nAfter adding 5 at start:")
print_list(head)
