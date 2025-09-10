#method 1
def reverse_arr(arr):
    return arr[::-1]
#method 2
def reverse_arr_1(arr):
    start=0
    end=len(arr)-1
    while start < end:
        arr[start],arr[end]=arr[end],arr[start]
        start +=1
        end -=1
    return arr
#example for method 1
arr=[1,2,3,4,5]
print(reverse_arr(arr))
#example for method 2
arr_2=[1,2,3,4,5]
print(reverse_arr_1(arr_2))
