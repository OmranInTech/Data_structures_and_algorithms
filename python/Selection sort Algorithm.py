#selection sort algorithm

#selection sort function                                
def selectionsort (arr):
   
   #declare the length of array
    n = len(arr)
    
    #perfom loop on each element in array
    for i in range(n):
        
        #value in index i will be condidered as minimum  value in array
        min_index=i
        
        #value index i will be comapred with other values in array
        for j in range(i+1,n):
            
            #if smaller value was found than index i value 
            if arr[j] < arr[min_index]:
                
                #so  new smaller value will be updated as minimum value
                min_index=j

        #now we will store small value in temp varibale
        temp=arr[min_index]
        #now we will asign small value to index i 
        arr[min_index]=arr[i]
        #now we will assign un sorted value in index i to minindex position
        arr[i]=temp

        #printin steps for better understanding
        print(f'step {i+1}: {arr}')

    #return arr    
    return arr

#example
array=[61,25,12,22,11]
print(selectionsort(array))
