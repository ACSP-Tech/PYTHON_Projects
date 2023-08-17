print("\n\nNUMBER GUESSING GAME...")
import random
num = random.randint(1,10)
guess = int(input("There are only 3 chances. \nGuess a number from 1 to 10: "))
if guess < num:
    print("your guess was smaller than the actual number!")
elif guess > num:
    print("Your guess was greater than the actual number!")
index = 0
while index <= 1:
    if guess == num:
        print("You guessed it correctly!")
        break
    print("your ", index + 2, " chance")
    guess = int(input("Try again, Guess a number from 1 to 10: "))
    if index == 1 and guess != num:
        print("wrong answer! the number is: ", num, "\nplay again! your 3 chances has been used up")
    elif guess < num:
        print("your guess was smaller than the actual number!")
    elif guess > num:
        print("Your guess was greater than the actual number!")
    elif guess == num:
        print("You guessed it correctly!")
        break
    index += 1
