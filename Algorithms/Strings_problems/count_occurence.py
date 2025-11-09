def count_occurence(s):
    counting={}

    for i in s:
        if i in counting:
            counting[i]+=1
        else:
            counting[i]=1
    return counting
# Test
print(count_occurence("hello"))  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}