def func1():
  try:
    li = [1, 2, 3, 4, 5]
    i = int(input("Enter the index: \n"))
    print(li[i])
    return 1
  except:
    print("Some error occured")
    return 0

  finally:
    print("I am always Executed")


l = func1()
print(l)
