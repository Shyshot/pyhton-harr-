marks = [11, 25, 67, 85, 98, 67, 90, 60]
# index = 0
# for mark in marks:
#   print(mark)
#   if (index == 3):
#     print("You are Half way there")
#   index += 1

# Using Enumerate Function the folloing code can be optimized into

for index, mark in enumerate(marks):
  print(mark)
  if (index == 3):
    print("You are Half way there")

