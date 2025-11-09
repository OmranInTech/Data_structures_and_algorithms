def count_vowel(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    return count


print(count_vowel("Hello World"))  # Output: 3
