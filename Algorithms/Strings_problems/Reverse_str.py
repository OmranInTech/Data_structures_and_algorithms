def reverse_str(s):
    reverse_st=''
    for i in range(len(s)-1,-1,-1):
        reverse_st +=s[i]
    if reverse_st==s:
        return True
    else:
        return False
    

print(reverse_str("khani"))  # Output: "dlroW olleH"