a = 668464
b = 41574

print("A") if a > b else print("=") if a == b else print("B")

# It is used to perform single linear condition.

# Consider the current clipboard:

def setAttribute(a, b):
  if a > b:
    return 1
  else:
    return 0


c = setAttribute(a, b)
print(c)

# The Above code can be written as:

c = 1 if a > b else 0
print(c)