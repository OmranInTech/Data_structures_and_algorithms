def remove_vowels_from_string(s):
    vowels='aeiouAEIOU'
    result = ''
    for i in s:
        if i not in vowels:
            result += i
    return result
# Test
print(remove_vowels_from_string("hello"))  # Output: "hll"
