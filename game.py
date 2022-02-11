import random
attempts1=[]
attempts3=[]
def game_start():
  attempts1=0 
  name=input("It seems like you are a bit bored.What is your name?")
  print("WELCOME TO THE GUESSING GAME, {}".format(name))
  random_number=(random.randint(1,10))
  random_number=int(random_number)
  print("Your record for trails is {}".format(attempts1))
  pick=input("Let's start the game. I've picked the number from 1-10. Which number is it?")

  try:
    pick=int(pick) 
  except ValueError:
    raise ValueError("Try to input integer value")
  pick=int(pick)
  while True:
    if pick>10:
      pick=input("Oh it seems like you enetered the value out of the range (1-10)try again: ")
      pick=int(pick)
    elif pick<0:
      pick=input("Oh it seems like you enetered the value out of the range (1-10)try again: ")
      pick=int(pick)
    else:
      break
  while pick !=random_number:
      attempts1 +=1
      if pick==random_number:
        print("Got it")
      elif pick<random_number:
        print("It's higher")
        pick=input("Pick again ")
        pick=int(pick)
      elif pick>random_number:
        print("It's lower")
        pick=input("Pick again ")
        pick=int(pick)
  else:
    print("The game is over {}. The number was {}.You used {} tries to guess the number. Thank you for playing".format(name,random_number,attempts1))

  attempts2=0
  again=input("Do you want to play again?\n(Enter y/n) ")
  again=again.lower()
  while again=="y":
    random_number=(random.randint(1,10))
    random_number=int(random_number)
    pick=input("Let's start the game. I've picked the number from 1-10. Which number is it? ")
    try:
      pick=int(pick) 
    except ValueError:
      raise ValueError("Try to input integer value")
    pick=int(pick)
    while True:
      if pick>10:
        pick=input("Oh it seems like you enetered the value out of the range (1-10)try again: ")
        pick=int(pick)
      elif pick<0:
       pick=input("Oh it seems like you enetered the value out of the range (1-10)try again: ")
       pick=int(pick)
      else:
        break
    
    while pick !=random_number:
        attempts2 +=1
        attempts3.append(attempts2)
        if pick==random_number:
          print("Got it")
        elif pick<random_number:
          print("It's higher")
          pick=input("Pick again ")
          pick=int(pick)  
        elif pick>random_number:
          print("It's lower")
          pick=input("Pick again ")
          pick=int(pick)
    print("The game is over {}. The number was {}.You used {} tries to guess the number. Thank you for playing".format(name,random_number, attempts3[-1]))
    again=input("Do you want to play adain?\n(Enter y/n) ")
  else:
    print("The game is over {}. The number was {}.You used {} tries to guess the number. Thank you for playing".format(name,random_number, attempts3[-1]))
  print("Thank you for playing my game")

game_start()
