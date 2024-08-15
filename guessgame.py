secret_number=9
i=0
while (i<=3):
  guess=int(input("Guess: "))
  i=i+1
  if(guess==secret_number):
    print("You win")
    break
else:
  print("You lose")

