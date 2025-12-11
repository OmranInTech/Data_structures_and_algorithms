def common_substr(main_substr,sub_substr):
    for i in main_substr:
        if i in sub_substr:
            return True
    return False
print(common_substr('hello','world'))  
