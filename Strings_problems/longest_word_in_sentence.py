def longest_word_in_sentence(s):
    words=s.split()
    longest=''
    for i in words:
        if len(i)>len(longest):
            longest=i
    return longest
print(longest_word_in_sentence('hello i am programmer'))