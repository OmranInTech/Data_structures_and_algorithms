def longest_repeating_substring(s):
    n = len(s)
    longest = ""
    for i in range(n):
        for j in range(i + 1, n + 1):
            substr = s[i:j]
            # Find another occurrence of the same substring after its end
            next_pos = s.find(substr, i + len(substr))
            if next_pos != -1 and len(substr) > len(longest):
                longest = substr
    return longest

print(longest_repeating_substring("banana"))  # Output: "an"
