def sum_pair_array(arr , k ):
    left=0
    right=len(arr)-1
    while left<right:
        if arr[left]+arr[right]==k:
            return True
        elif arr[left]+arr[right]>k:
            right-=1
        else:
            left+=1
    return False
# Example usage
print(sum_pair_array([1,2,3,4,5],9))  # Output: True
