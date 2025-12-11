def remove_duplicate_from_str(s):
    st=''
    for i in s:
        if i not in st:
            st+=i

    return st
print(remove_duplicate_from_str('banaa'
)) 