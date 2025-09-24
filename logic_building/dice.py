def dic_problem(n):

    if n==1:
        return 6
    elif n==2:
        return 5
    elif n==3:
        return 4
    elif n==4:
        return 3
    elif n==5:
        return 2
    elif n==6:
        return 1
    else:
        return "Invalid input"  
    
# Example usage:
n = 3
result = dic_problem(n)
print(f"The opposite face of the die showing {n} is {result}.")
