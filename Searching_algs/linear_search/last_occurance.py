#last occurrence
def last_occurrence(arr, k):
    current_position = -1   # -1 means "not found"
    for i in range(len(arr)):
        if arr[i] == k:
            current_position = i
    return current_position
# Example usage
print(last_occurrence([1, 3, 3, 4, 5], 3))  # Output: 2
