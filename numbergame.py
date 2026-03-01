import random

num = random.randint(1,30)
guess = "none"
while guess != num:
    guess = int(input("Enter the number between 1 and 30 : "))
    if guess == num:
        print("Congratulations!")
        print("You have guessed the correct number")
    elif guess > num:
        print("Oops, you guessed the wrong number")
        print("Please Guess a lower number")
    else:
         print("Oops, you guessed the wrong number")
         print("Please Guess a higher number")

