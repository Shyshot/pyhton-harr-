# a = (input("Enter the Number"))

# print(f"Multiplication table of {a} is:")

# try:
#   for i in range(1, 11):
#     print(f"{int(a)}x{i} = {i*int(a)}")
# except Exception as e:  #If you Dont't want to use the the error from the terminal then there is no neccesity to use the Exception as e
#   print(f"Tere Baap ne banaya tha kya {a} ka table")

# print("Some Important lines of code")
# print("End of program")

try:
  num = int(input("Enter a Integer:"))
  a = [6, 3]
  print(a[num])
except ValueError:
  print("Number entered is not an integer ")
except IndexError:
  print("Index Error")
