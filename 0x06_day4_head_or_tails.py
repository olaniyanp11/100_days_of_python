#!/usr/bin/python3
import random



your_input = input("welcome to the heads or tails game \nyou are expected to choose heads or tails,\n if the computer generate your choice you win:")
your_input = your_input.lower()
comp = random.randint(1,20)
if comp % 2:
    me = 'head'
else:
    me = 'tails'
if me == your_input:
    print("you win")
else:
    print("you loose")
    print(f"{me} was chosen")
