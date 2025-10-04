#reverse_string
s = "hello"
stack = []
for char in s:
    stack.append(char)
reversed_s = ""
while stack:
    reversed_s += stack.pop()
print(reversed_s)
