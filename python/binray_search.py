#binary search algorithm for a sorted array 

def binary_search_fun (arr,target_value):
    low =0
    high=len(arr)+1
    while low <= high:
        mid=(low+high)//2
        guess=arr[mid]
        if target_value == guess:
            return mid 
        elif target_value > guess:
            low= mid +1
        else:
            high= mid -1      
    return None 


#implementation of binary search function 

sorted_arr=[1,2,3,4,5,6,7,8]
print(binary_search_fun(sorted_arr,5))
