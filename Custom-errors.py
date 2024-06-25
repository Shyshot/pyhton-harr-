#It is used to stop a python program at the point to error and avoiding further damage

a = int(input("Enter a number greater then 1"))
if (a < 1):
  raise ValueError("Number should be greater then 1")

while (True):
  print(a)
  if (a == 1):
    break
  a -= 1