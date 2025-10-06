def max_value_less_thanK(arr,k):
    max_value=0
    for i in arr:
        if i >max_value and i<k:
            max_value=i
    return max_value
#example usage
print(max_value_less_thanK([1,2,3,4,5],3))  #Output: 2