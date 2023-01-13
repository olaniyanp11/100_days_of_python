#!/usr/bin/python3
""""
randomise the paying of a reasturant bill
"""
import random

def ranom(bowl):
    """
    returns a random person to pay the bills
    """
    payer =0
    payer = random.randint(0,len(bowl)-1)
    return bowl[payer]
bowl = input("the list of people seperated by a comma Eg ayo,boy:\n")
bowl = bowl.split(',')
bowl = ranom(bowl)
print(bowl)
