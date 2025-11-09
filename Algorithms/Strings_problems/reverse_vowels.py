def reverse_vowels_whilekeepingother(s):
    vowels = 'aeiouAEIOU'
    s_vowels = []
    
    # Step 1: collect vowels
    for char in s:
        if char in vowels:
            s_vowels.append(char)
    
    # reverse vowels
    s_vowels = s_vowels[::-1]
    
    # Step 2: build final string
    s_final_str = ''
    vowel_index = 0
    
    for char in s:
        if char in vowels:
            s_final_str += s_vowels[vowel_index]
            vowel_index += 1
        else:
            s_final_str += char
    
    return s_final_str

# Test
print(reverse_vowels_whilekeepingother("hello"))  # Output: "holle"
print(reverse_vowels_whilekeepingother("Omran"))  # Output: "Omran" (only one vowel reversed)
