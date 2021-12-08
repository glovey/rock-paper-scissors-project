# rock, paper, scissors!!

import random
winners = {"r":"s","s":"p","p":"r"}


def new_game():
  win = 0
  lose = 0

  choice = ["r", "p", "s"]
  name = input("Hello what's your name?")
  start = input(f"do you want to play a game {name}? Enter yes or no")
  
  while start == "yes":
    computer = choice[int(random.randint(0,2))]
    guess = input("time to choose! pick r, p or s")
    if guess == computer:
      print (f"I picked {computer}!")
      print ("its a draw!")
      start = input("do you want to play again? yes or no")
    elif winners[guess] == computer:
      print (f"I picked {computer}!")
      print ("Damn, you win!!")
      win += 1
      start = input("do you want to play again? yes or no")
    else:
      print (f"I picked {computer}!")
      print ("I win, loser!")
      lose += 1
      start = input("do you want to play again? yes or no")
  else:
    print (f"no worries, the final scores were {win} win(s) to you and {lose} win(s) to me")

new_game()
