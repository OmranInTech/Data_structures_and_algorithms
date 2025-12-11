def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        pivot = (left + right) // 2
        if arr[pivot] == target:
            return pivot   # return index
        elif arr[pivot] > target:
            right = pivot - 1
        else:
            left = pivot + 1
    return -1

# Example usage
print(binary_search([1, 2, 3, 4, 5], 3))  # Output: 2
