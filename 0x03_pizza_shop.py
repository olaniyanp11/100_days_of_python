#!/usr/bin/python3

print("welcome to python pizza deliveries!")
size = input("what size of pizza do you want?\nsmall medium or large: ")
bill = 0
if size == 'small':
    bill = 15
    add_pepperoni = input("do you want pepperoni? :")
    if add_pepperoni == 'yes':
        bill += 2
    extra_cheese = input("do you want extra cheese")
    if extra_cheese == 'yes'and bill != 0:
        bill += 1
elif size == 'medium':
    bill = 20
    add_pepperoni = input("do you want pepperoni? :")
    if add_pepperoni == 'yes':
        bill += 3
    extra_cheese = input("do you want extra cheese")
    if extra_cheese == 'yes'and bill != 0:
        bill += 1
elif size == 'large':
    bill = 25
    add_pepperoni = input("do you want pepperoni? :")
    if add_pepperoni == 'yes':
        bill += 3
    extra_cheese = input("do you want extra cheese")
    if extra_cheese == 'yes'and bill != 0:
        bill += 1
print(f"your bill is ${bill}")
