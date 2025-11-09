def convert_str_to_alterantive_case(s):
    converted_str=''
    for i in range(len(s)):
        if i%2==0:
            converted_str+=s[i].upper()
        else:
            converted_str+=s[i].lower()
    return converted_str
print(convert_str_to_alterantive_case('hello'))
