# Function to implement binary search
def binary_search(lst, element):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]

        if guess == element:
            return mid
        elif guess > element:
            high = mid - 1  # Fix: should adjust 'high', not return mid-1
        else:
            low = mid + 1

    return None


mylist = [1, 2, 3, 4, 5, 6]
#calling function
result = binary_search(mylist, 5)
print(result)
