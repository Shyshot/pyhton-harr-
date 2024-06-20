# x = 4

# match x:
#   case 0:
#     print("X ix Zero")

#   case 4:
#     print("X % 2 == 0 and case is 4")


print("Do you to Vote\n")
Choice = int(input("Enter 1 for Yes and 0 for No\n"))

def Voting():
  try:
    Vote = int(
      input(
        "Enter Your Vote By typing the number of the respective party\n"))
  except ValueError:
    print("Please Enter The Number Wrriten before the party name")
    Voting()
  Result(Vote)
def CheckResults(BJP,Congress,AAP,NOTA):
  try:
   PassWord = int(input("Enter The Password To Check The Results\n"))
  except:
    print("Wrong Password")
    CheckResults(BJP,Congress,AAP,NOTA)
  if PassWord == 312006:
    print("BJP = ", BJP)
    print("Congress = ", Congress)
    print("AAP = ", AAP)
    print("NOTA = ", NOTA)
  else:
    print("Wrong Password")
    CheckResults(BJP,Congress,AAP,NOTA)
def Result(Vote):
  BJP = 0
  Congress = 0
  AAP = 0
  NOTA = 0
  match Vote:
    case 1:
      print("You Voted For BJP")
      BJP += 1
    case 2:
      print("You Voted For Congress")
      Congress += 1
    case 3:
      print("You Voted For AAP")
      AAP += 1
    case 4:
      print("You Voted For NOTA")
      NOTA += 1
  if(Vote > 4) :
    print("Please Enter a Valid Number")
    Voting()
  else:
    print("Thank You For Voting")
    CheckResults(BJP,Congress,AAP,NOTA)
if(Choice == 0):
    print("Thanks For Visiting")
else:
    print("You Options Are \n 1.BJP \n 2.Congress \n 3.AAP \n 4.NOTA \n")
    Voting()


