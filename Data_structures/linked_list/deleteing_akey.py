
node1 = [10, None]
node2 = [20, None]
node3 = [30, None]

node1[1] = node2
node2[1] = node3

head = node1

def deleting(head, value):
    # Special case: if head needs to be deleted
    if head is None:
        return head
    
    if head[0] == value:
        return head[1]  # move head to next node
    
    current = head
    while current[1] is not None:
        if current[1][0] == value:
            # Skip the node to be deleted
            current[1] = current[1][1]
            return head
        current = current[1]
    
    # If value not found, just return the original head
    return head

head = deleting(head, 10)  # Delete node with value 10

# Function to print list to verify
def print_list(head):
    current = head
    while current is not None:
        print(current[0], end=" -> ")
        current = current[1]
    print("None")

print_list(head)
