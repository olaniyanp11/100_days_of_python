#!/usr/bin/python3
import random


print("welcome to the game of rock paper scissors")
user_choice = (input("you are expected to enter an input\
        \nRock, paper or scissors: \n"))
user_choice = user_choice.lower()

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
rock
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
paper
'''

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
scissors
"""
computer = [rock, paper, scissors]
ans = random.choice(computer)
if user_choice == 'rock':
    user_choice = rock
elif user_choice == 'paper':
    user_choice = paper
elif user_choice == 'scissors':
    user_choice = scissors
# selecting the winner
if (user_choice == rock) or (user_choice == paper) or (user_choice == scissors):
    if (ans == scissors) and (user_choice == paper):
        print(f"You chose {user_choice} and the computer chose{ans}\n You lose")
    elif (ans == rock) and (user_choice == scissors):
        print(f"You chose {user_choice} and the computer chose{ans}\n You lose")
    elif (ans == user_choice):
        print(f"You chose {user_choice} and the computer chose{ans}\n its a draw")
    elif (ans == paper) and (user_choice == rock):
        print(f"You chose {user_choice} and the computer chose{ans}\n You lose")
    else:
        print(f"You chose {user_choice} and the computer chose{ans}\n You win")
else:
    print("you entered an invalid input")
    print(f"The computer chose{ans}\n You lose")
