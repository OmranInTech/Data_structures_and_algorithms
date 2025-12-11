def replace_substr_with_another(main_str, old_substr, new_substr):
    return main_str.replace(old_substr, new_substr)
print(replace_substr_with_another('hello world', 'world', 'there'))  # Output: hello there