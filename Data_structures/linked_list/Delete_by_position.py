def delete_by_position(head, position):
    if head is None:
        return head

    # If deleting the head node
    if position == 0:
        return head[1]

    current = head
    count = 0

    # Traverse to the node before the one to delete
    while current is not None and count < position - 1:
        current = current[1]
        count += 1

    # If position is out of range or next node is None, do nothing
    if current is None or current[1] is None:
        return head

    # Bypass the node at 'position'
    current[1] = current[1][1]

    return head

def print_list(head):
    current = head
    while current is not None:
        print(current[0], end=" -> ")
        current = current[1]
    print("None")


# Example usage:
node1 = [10, None]
node2 = [20, None]
node3 = [30, None]
node4 = [40, None]

node1[1] = node2
node2[1] = node3
node3[1] = node4

head = node1

print("Original list:")
print_list(head)

head = delete_by_position(head, 2)  # Delete node at position 2 (0-based)

print("After deleting node at position 2:")
print_list(head)
