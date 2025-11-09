def substr_(main,sub):
    first_index=-1
    for i in range(len(main)-len(sub)+1):
        if main[i:i+len(sub)]==sub:
            first_index=i
            break

    return first_index
print(substr_('hello world world','world'))  # Output: 6