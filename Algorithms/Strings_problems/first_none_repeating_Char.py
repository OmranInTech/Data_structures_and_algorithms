def first_none_rep(s):
    chars={}
    for i in s:
        if i in chars:
            chars[i]+=1
        else:
            chars[i]=1
    for j in chars:
        if chars[j]==1:
            return j
    return None
# Test
print(first_none_rep("swiss"))  # Output: "w"