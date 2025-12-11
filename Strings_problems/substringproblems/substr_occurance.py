def substr_occurence (main,sub):

    count=0
    for i in range(len(main)-len(sub)+1):
        if main[i:i+len(sub)]==sub:
            count+=1
    return count
print(substr_occurence('hello world world','world'))  # Output: 2