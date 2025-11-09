def count_vowel_constants(s):
    vowerl='aeiouAEIOU'
    constant='bcdfghjklmnpqrstvwxyz'
    vowel_count=0
    constant_count=0
    for i in s:
        if i in vowerl:
            vowel_count +=1
        elif i in constant:
            constant_count +=1
    
    return 'vowel : ',vowel_count,'constant',constant_count
print(count_vowel_constants('hello'))
