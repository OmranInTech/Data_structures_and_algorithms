def max_queue(qeue):
    #function 
    max_value=0
    for i in qeue:
        if i > max_value:
            max_value=i
    return max_value
#example usage
print(max_queue([1,2,3,4]))
