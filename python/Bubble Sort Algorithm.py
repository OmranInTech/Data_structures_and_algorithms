                                            #bubble sort 

def bubblesort(arr):

    n=len(arr)
    
    #repeat process for each element 
    for i in range(n):

        #go throw unsorted element
        for j in range(0,n-i-1):
            
            #compare adjusent elements
            if arr[j]>arr[j+1]:
                
                #swap if element was greater than next element
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp

            #print steps 
            print(f'steps  {i+1}: {arr}')
    return arr


numberrs = [64, 34, 25, 12, 22, 11, 90]
print(bubblesort(numberrs))