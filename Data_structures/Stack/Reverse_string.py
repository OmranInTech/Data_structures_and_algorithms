# Input string
s = "hello"

# Use a stack (list)
stack = []

# Push all characters onto the stack
for char in s:
    stack.append(char)

# Pop characters to reverse the string
reversed_s = ""
while stack:
    reversed_s += stack.pop()

print(reversed_s)
