def most_frequent_char_in_word(s):
    frequent_letter={}
    for i in s:
        if i in frequent_letter:
            frequent_letter[i]+=1
        else:
            frequent_letter[i]=1
    most_char=None
    highest=0
    for ch  in frequent_letter:
        if frequent_letter[ch]>highest:
            highest=frequent_letter[ch]
            most_char=ch
    return most_char


print(most_frequent_char_in_word('hellee'))