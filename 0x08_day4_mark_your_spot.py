#!/usr/bin/python3
print("welcome to x marking gaming where youd make a mark in the matrix below:\
        \n Note the rows are numbered 1-3 and columns 1-3")
row1 = ['q', 'q', 'q']
row2 = ['q', 'q', 'q']
row3 = ['q', 'q', 'q']
map = [row1, row2, row3]
print(f"1. {row1}\n2. {row2}\n3. {row3}""")


spot = input("where do you want to put your treasure")
map[int(spot[0]) - 1][int(spot[1]) - 1] = "x"
print(f"{row1}\n{row2}\n{row3}""")
