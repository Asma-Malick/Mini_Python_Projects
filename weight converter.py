weight=input("Weight: ")
unit=input("(L)bs or (K)g: ")
if unit.upper()=="L":
  converted=float(weight)*0.45
  print(f"You are {converted} kilos")
elif unit.upper()=="K":
  converted=float(weight)/0.45
  print(f"You are {converted} pounds")
else:
  print("Invalid input")