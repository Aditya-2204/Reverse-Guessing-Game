'''
Aditya Chakraborty
9/7/23
Reverse Guess The number
'''
import random

l_limit = 1
h_limit = 100
randomNumber = random.randint(l_limit, h_limit)
input("Pick a number from 1-100 and press enter")
res = input(f"Is it {randomNumber}. Enter h if its too high, enter l if too low or g if I got it.")
running=True
while running:
    if res == "l":
        l_limit = randomNumber-1
        randomNumber = random.randint(l_limit, h_limit)
        res = input(f"Is it {randomNumber}: ")

    elif res == "h":
        h_limit = randomNumber-1
        randomNumber = random.randint(l_limit, h_limit)
        res = input(f"Is it {randomNumber}: ")

    if res == "g":
        print("I win!")
        running=False
        
