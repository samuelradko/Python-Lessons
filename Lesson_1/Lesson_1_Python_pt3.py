#[Q1] Write a Python program that receives an integer from the variable and prints its square

n = input("Please type a number: ") # User input
n = int(n) # convert to int
n = n ** 2 # Takes the user input and prints its square
print(n) # final resuolt 

#[Q2] Write a program in Python that receives a 3-digit number from the user and prints the sum of its digits with a for loop

Num = input("Please type any 3-digit number: ")
Num = int(Num)
Sum = Num%10
Num //= 10
Sum += Num%10
n //= 10
Sum += n%10
print(Sum)