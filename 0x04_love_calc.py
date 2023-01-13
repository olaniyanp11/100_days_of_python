#!/usr/bin/python3

print("welcome to the love calculator!")
name1= input("what is your name!\n")
name2 = input("what is their name!\n")
love = "love"
true = "true"
ans1 =0
ans2 = 0
name1 = name1.lower()
name2 = name2.lower()
for i in love:
    ans1 += name1.count(i)
    ans1 += name2.count(i)
for j in true:
    ans2 += name1.count(j)
    ans2 += name2.count(j)
score = str(ans2) + str(ans1)
score = int(score)
if score < 10 or score >90:
    print(f"your score is {score}, you go together like coke and mentos")
if score >=40 and score < 51:
    print(f"your score is {score}, you are alright together.")
else:
    print(f"your score is {score}")
