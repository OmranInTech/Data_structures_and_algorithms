def first_occurence(arr,k):
    for i in arr:
        if arr[i]==k:
            return i
    return -1
#example usage
print(first_occurence([1,3,3,4,5],3))  