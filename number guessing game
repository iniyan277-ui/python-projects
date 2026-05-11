import random
import time

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num, highest_num)

print("Guess the number!!!")
time.sleep(2)
guess=0
try:
    num_of_guesses = 0
    while guess != answer:
     guess = int(input(f"Enter your guess({lowest_num} to {highest_num}): "))
     if guess < lowest_num or guess > highest_num:
         print("your guess is not valid")
     elif guess > answer:
         print("your guess is too high")
     elif guess < answer:
         print("your guess is too low")
     else:
         print("your guess is correct")
     num_of_guesses += 1

except ValueError:
    print("Please enter a valid number")

print(f"total no of guesses : {num_of_guesses}")
