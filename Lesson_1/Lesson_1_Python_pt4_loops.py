#[Q1] Write a program in Python that receives a N-digit number from the user and prints the sum of its digits

# number = input("Enter a N-digit number: ")
# sum = 0 # variable "sum" used to store the sum of the digits of the input number.
# for digit in number: # for loop which iterates through each character in the string `number`.
#     sum += int(digit) # converts the current character in `number` from a string to an integer and adds it to the `sum`.
# print("The sum of the digits is:", sum) # Prints the final sum that the user has typed.

import random
number = random.randint(1, 10)
guess_num = input("Guess a number between 1-10: ")

if int(guess_num) == number:
    print("You guessed it right!")
    print("The number was", number)
    
elif int(guess_num) > number:
    print("You guessed it wrong!")
    print("The number was", number)
    difference = abs(int(guess_num) - number)
    print("You were off by", difference)