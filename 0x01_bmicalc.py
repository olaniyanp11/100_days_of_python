#!/usr/bin/python3

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

ans = weight / (height ** 2)
if ans < 18.5:
    print("you are underweight")
elif ans < 25:
    print("you have a normal weight")
elif ans < 30:
    print("you are overweight")
elif ans <35:
    print("you are obese")
else:
    print("you are clinically obese")
