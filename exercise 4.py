
print("exercise 4")
import random
number = random.randint(1,10)
guess = int(input("Guess a number from 1 to 10: "))
while guess != number:
    if guess < number:
        print("too low")
    if guess > number:
        print("too high")
    guess = int(input("Guess a number from 1 to 10: "))
if guess == number:
    print("Correct")