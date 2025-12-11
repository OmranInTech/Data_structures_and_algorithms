def compress_str(s):
    final_str=''
    count=1
    prev=s[0]
    for i in s[1:]:
        if i==prev:
            count+=1
        else:
            final_str += prev + str(count)
            prev=i
            count=1
    final_str += prev + str(count)
    return final_str
print(compress_str('aaabbcdddde'))  # Output: a3b2c1d4e1

