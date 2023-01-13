#!/usr/bin/python3

year = int(input("check your year: "))
if year % 4 ==0:
    print("its a leap year")
elif year % 100 == 0:
    print("its a leap year")
elif year % 400 == 0:
    print("its a leap year")
else:
    print("its not a leap year")

