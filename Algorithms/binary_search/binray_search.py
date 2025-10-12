def binary_search(arr, target):
    """
    Perform binary search on a sorted array.
    Parameters:
        arr (list): A sorted list of elements.
        target: The value to search for.
    Returns:
        int: The index of target in arr if found, else None.
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if target == guess:
            return mid
        elif target > guess:
            low = mid + 1
        else:
            high = mid - 1
    return None

# Example usage: Find 5 in the sorted array
sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(binary_search(sorted_arr, 5))  # Output: 4
