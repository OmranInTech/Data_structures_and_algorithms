def valid_parentheses(s):
  #this function will help us to find the valid parentheses
  stack=[]
  parents={
  ')':'(',
  '}':'{',
  ']':'['
  }
  for char in s:
    if char in parents:
      top=stack.pop() if stack else '#'
      if parents[char] != top:
        return False
    else:
      stack.append(char)
  return not stack
#example usage 
s='()[]{}'
print(valid_parentheses(s))
