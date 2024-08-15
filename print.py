name=input("what is your name? ")
name2=len(name)
if name2 < 3:
  print("your name is too short")
elif name2 >50:
  print("your name is too long")
else:
  print("your name is just right")