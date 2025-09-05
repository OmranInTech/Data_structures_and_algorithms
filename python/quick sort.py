#quick sort algorithm

#quick sort funciton
def quicksort(arr):
    #we use this condition for array that has one element so the array is already sorted
    if len(arr) <=1:
        return arr

    #we have to select pivot and smaller and larger array 
    pivot = arr[len(arr)//2]
    smaller = []
    larger = []

    #we will shift element > pivot to larger array and element< pivot to smaller array 
    for i in range(len(arr)):
        if arr[i]==pivot:
            continue
        elif arr[i]<pivot:
            smaller.append(arr[i])
        else:
            larger.append(arr[i])

  
    sorted_smaller = quicksort(smaller)
    sorted_larger  = quicksort(larger)

    #combine of pivotes 
    return sorted_smaller+ [pivot] +sorted_larger

#use of  function of quick sort
numbers=[8,2,43,2,12,645,231,122,9]
print(f'Original numbers ' ,numbers)
print('sorted numbers : ',quicksort(numbers))
