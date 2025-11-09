def check_substr (main,sub):

    for i in range(len(main)-len(sub)+1):
        if main[i:i+len(sub)]==sub:
            return True
    return False

    
print(check_substr('hello world','world'))  # Output: True