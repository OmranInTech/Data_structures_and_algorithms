
#function for to implement binary search
def binary_search (list,element):
    low =0
    high = len(list) -1

    while low <= high:
        mid = (low+high) //2
        guess=list[mid]

        if guess == element:
            return mid
        if guess> element:
            return mid-1
        else:
            low=mid+1

        
    return None


mylist=[1,2,3,4,5,6]
result=binary_search(mylist,5)
print(result)


