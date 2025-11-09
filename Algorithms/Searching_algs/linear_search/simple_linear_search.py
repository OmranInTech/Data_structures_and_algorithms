def linear_search(arr,k):
    for i in arr:
        if arr[i]==k:
            return arr[i] 
    return -1
#example usage
print(linear_search([1,2,3,4,5],3))  #Output: 3