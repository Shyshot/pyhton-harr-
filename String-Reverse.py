# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

message = str(input("Enter your message: "))


def decode(message):
  message = message[3:-3]
  message = message[-1] + message[:-1]
  print(message)


if len(message) >= 3:
  message = message[1:] + message[0]
  message = "abc" + message + "xyz"
  print(message)
else:
  message = message[::-1]
  print(message)
try:
  permisson = int(
    input("Do you Want to Decode the message 1 for yes and 0 for no:"))
  if permisson == 1:
    decode(message)
  else:
    print("Thank you")
except:
  print("You have entered a wrong input")
