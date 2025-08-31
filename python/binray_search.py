#binary_search_algorithm
def binary_search(sorted_list: list[int], target: int) -> int | None:
    """
    Performs binary search on a sorted list.

    Args:
        sorted_list (list[int]): The list to search (must be sorted).
        target (int): The value to search for.

    Returns:
        int | None: The index of target if found, else None.
    """
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = sorted_list[mid]

        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return None

#use of binary search function
a_list = [1, 2, 3, 4, 5, 6]
result = binary_search(a_list, 5)
print(result)
