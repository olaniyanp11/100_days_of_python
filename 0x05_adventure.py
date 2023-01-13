#!/usr/bin/python3
print("--------------\n-------------\n-----------\n---------\n-------\n-----\n---\n-\n")
print("welcome to Tresure island your mission is to find the tresure!!!!")
direction1 = input("you are in a jungle with no resources an you have two option : go left into the river OR go right into a cave")
direction1 = direction1.lower()

if direction1 == 'right':
    direction2 = input("crossing the river u saw something coming out of the river and you are left with two options \n : Swim OR Wait?:\n ")
    if direction2 == 'wait':
        direction3 = input("Hurray you were patient enough to meet the wizard coming out of the water ,he then showed you three stones :\nRed,Yellow,blue \nto which contains the three tresure and you were asked to break one which would you choose?: \n")
        if direction3 == 'yellow':
            print('congratulations \nyou\'ve \n got \ngold\n')
        elif direction3 == 'blue':
            ('you hatched the egg of an angry shark \tGame \tover')
        else:
            print('you angered the wizard \n\tGame over')
    else:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b\byou were swallowed by a moving whale")
else:
    print("you were eaten by a leopard Game Over")
