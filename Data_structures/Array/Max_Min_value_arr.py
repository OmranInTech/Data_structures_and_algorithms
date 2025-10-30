def max_min_value_array(arr):
    max_value = arr[0]
    min_value = arr[0]
    for i in arr:
        if i > max_value:
            max_value = i
        if i < min_value:
            min_value = i
    return max_value, min_value
# Example :
arr = [3, 7, 1, 9, -2]
max_val, min_val = max_min_value_array(arr)
print("Max:", max_val)
print("Min:", min_val)
