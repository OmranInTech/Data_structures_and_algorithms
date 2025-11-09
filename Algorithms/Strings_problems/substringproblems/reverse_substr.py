def reverse_substr_inside_str(main_str,start,end):
    sub_str_=main_str[start:end+1]
    reversed_substr=sub_str_[::-1]
    return main_str[:start]+reversed_substr+main_str[end+1:]
print(reverse_substr_inside_str('hello world',0,4))  # Output: olleh world