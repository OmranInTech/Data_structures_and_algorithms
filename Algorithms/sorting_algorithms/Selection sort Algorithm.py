def selection_sort(arr):
    """
    Sorts a list in ascending order using the Selection Sort algorithm.

    Parameters:
    arr (list): The list of numbers to sort.

    Returns:
    list: Sorted list in ascending order.

    Notes:
    In-place algorithm: modifies the original list.
    """
    n = len(arr)
    for i in range(n):
        min_index = i  # Assume current index is minimum
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j  # Found new minimum
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap
    return arr

if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Original array:", arr)
    sorted_arr = selection_sort(arr)
    print("Sorted array:", sorted_arr)
