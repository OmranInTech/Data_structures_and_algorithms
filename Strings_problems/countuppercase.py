def count_uppecase(s):
    count=0
    for i in s:
        if i.isupper():
            count+=1
    return count
print(count_uppecase("Hello World"))  # Output: 2