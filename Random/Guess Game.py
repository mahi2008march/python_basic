import random
import time
actual_num=random.randint(1,9)
guess=0
count=0

while guess != actual_num and guess != "exit":
    guess = input("Guess a number from 1 to 10? or type \"exit\" to exit out of game\t")
    if guess == "exit":
        break
    guess = int(guess)
    count += 1

    if guess < actual_num:
        print("Too low!")
    elif guess > actual_num:
        print("Too high!")
    else:
        print("Congratulations ! You got it!")
        print("And it only took you", count, "tries!")
        time.sleep(10)
