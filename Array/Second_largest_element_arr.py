def second_largest(arr):
    '''this function will find second large element in an array'''
    max_value = arr[0]
    for i in arr:
        if i > max_value:
            max_value = i
    second_largest = None  
    for i in arr:
        if i < max_value:
            if second_largest is None or i > second_largest:
                second_largest = i
    return second_largest
#exmaple usage
arr = [1,2,3,4,5,6]
print(second_largest(arr))
