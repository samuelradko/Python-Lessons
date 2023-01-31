# # [Q1] Printing the numbers 1 to 10 using for loops

for i in range(1, 11):
    if i < 11:
        print(i)

# # [Q2] Calculating the sum of numbers 1 to 100 using a for loop:

sum = 0
for i in range(101):
    sum += i
print(sum)


# # [Q3] Printing all even numbers from 1 to 20 using a for loop:

for i in range(1, 21, 2):
    print(i)


# # [Q4] Printing the multiplication table of a given number using a for loop:

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num*i)

# [Q5] Printing the elements of a list using a for loop:

numbers = ["John","Will","Adam","Mat"]
for i in numbers:
    for j in i:
     print(j)

#[Q6 - Self question] By using "slicing" make any elements list and use the slice operator

numbers2 = [1,2,3,4,5,6,7,8,9,10]
names = ["John","Will","Adam","Mat","Samuel","Sergay"]
print(numbers2[3:])
print(names[2:4])


# Harder Q'z

# [Q1] Printing the first n fibonacci numbers using a for loop:



# [Q2] Printing the prime numbers between a given range using a for loop:



# [Q3] {fix the bugs!} Printing the elements of a nested list using a for loop:

numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for lst in numbers:
    for num in lst:
        print(lst)


# [Q4] { fix the bugs! } Flattening a nested list using a for loop:

numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = []
for lst in numbers:
    for num in lst:
        flat_list.append(num)
print(flat_list)


# # [Q5] Printing the frequency of each element in a list using a for loop:


numbers = [1, 2, 3, 4, 2, 1, 4, 4, 5, 1]
freq = {}

for i in range(len(numbers)):
    if numbers[i] in freq:
        freq[numbers[i]] += 1
    else:
        freq[numbers[i]] = 1
        
print(freq)