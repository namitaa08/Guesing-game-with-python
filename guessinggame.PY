import random

guess = 0
tries = 0

number = random.randint(1,10)

name = input("Hello, May i know your name?")
print("Hello "+name+".")

question = input("Are you ready to guess? [Y/N]")

if question.lower() == 'n':
    print("I'm sorry , we'll meet each other next time!!")
    exit()
if question.lower() == 'y':
    print("Guess a number between 1 & 10")


while not(guess == number):
    guess = int(input("What's your guess?"))
    tries = tries+1
    if guess == number:
        print("Brilliant!!")
        print("Congrats your guess was correct, your number is indeed {}".format(number))
        print("It has taken you {} tries".format(tries))
    elif guess < number:
        print("No! Guess a higher number") 
    elif guess > number:
        print("No! Guess a smaller number ")   

