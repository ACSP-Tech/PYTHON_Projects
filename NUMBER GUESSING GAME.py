import random
index = 0
num = random.randint(1,10)
while index <= 2:
    var = index + 1 
    guess = int(input("There are only 3 chances. Guess a number from 1 to 10: "))
    if guess == num:
        print("You guessed it correctly!")
        break
    if index == 2 and guess != num:
        print("wrong answer! the number is: ", num, "\nplay again! your 3 chances has been used up")
    elif guess < num:
        print("your guess was smaller than the actual number!. This is your", var, "attempt" )
    elif guess > num:
        print("Your guess was greater than the actual number!. This is your", var, "attempt")
    index += 1
