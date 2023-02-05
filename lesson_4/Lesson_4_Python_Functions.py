"""
Write a function that takes a string as input and returns a string with all vowels removed.
Write a function that takes a number as input and returns its factorial.
Write a function that takes two lists of equal length as input and returns a new list containing the elements of both lists, alternating between the two.
Write a function that takes a string as input and returns the number of times a specific character appears in the string.
Write a function that takes a number as input and returns its Fibonacci sequence up to that number.
Write a function that takes a list of numbers as input and returns the largest number in the list.
Write a function that takes a string as input and returns a string with all vowels replaced with 'x'.
Write a function that takes a list of numbers as input and returns the sum of all the even numbers in the list.
Write a function that takes two strings as input and returns a string with the first string repeated the number of times specified by the second string.
Write a function that takes a list of numbers as input and returns a new list with all duplicates removed
"""

# [Q1] Write a function that takes a string as input and returns a string with all vowels removed.
s = "A1"
print(s.title().center(50, "-"))


def rem_vow(mystr):
    vowels = 'aeiouAEIOU'
    mylist = []
    for i in mystr:
        if i not in vowels:
            mylist.append(i)
    return "".join(mylist)


print(rem_vow("pokemon"))


# [Q2] Write a function that takes a number as input and returns its factorial.
s = "A2"
print(s.title().center(50, "-"))


def factorial(n):

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(5))


# [Q3] Write a function that takes two lists of equal length as input and returns a new list containing the elements of both lists, alternating between the two.
s = "A3"
print(s.title().center(50, "-"))


def alternating(mylist1, mylist2):
    mylist = []
    for i in range(len(mylist1)):
        mylist.append(mylist1[i])
        mylist.append(mylist2[i])
        return mylist


print(alternating([1, 2, 3], [4, 5, 6]))


# [Q4] Write a function that takes a string as input and returns the number of times a specific character appears in the string.
s = "A4"
print(s.title().center(50, "-"))


def count_char(mystr, char):
    return mystr.count(char)


print(count_char("pokemon", "p"))


# [Q5] Write a function that takes a number as input and returns its Fibonacci sequence up to that number.
s = "A5"
print(s.title().center(50, "-"))


def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            next_number = fib_sequence[i-1] + fib_sequence[i-2]
            if next_number > n:
                break
            fib_sequence.append(next_number)
        return fib_sequence


print(fibonacci(10))


# [Q6] Write a function that takes a list of numbers as input and returns the largest number in the list.
s = "A6"
print(s.title().center(50, "-"))


def largest(mylist):
    if len(mylist) == 0:
        return 0
    elif len(mylist) == 1:
        return mylist[0]
    else:
        return max(mylist[0], largest(mylist[1:]))


print(largest([1, 2, 3, 4, 5]))


# [Q7] Write a function that takes a string as input and returns a string with all vowels replaced with 'x'
s = "A7"
print(s.title().center(50, "-"))


def replace_vow(mystr):
    vowels = 'aeiouAEIOU'
    mylist = []
    for i in mystr:
        if i in vowels:
            mylist.append('x')
        else:
            mylist.append(i)
    return "".join(mylist)


print(replace_vow("pokemon"))


# [Q8] Write a function that takes a list of numbers as input and returns the sum of all the even numbers in the list.
s = "A8"
print(s.title().center(50, "-"))


def sum_even(mylist):
    sum = 0
    for i in mylist:
        if i % 2 == 0:
            sum += i
            return sum


print(sum_even([1, 2, 3, 4, 5, 6, 7]))


# [Q9] Write a function that takes two strings as input and returns a string with the first string repeated the number of times specified by the second string.
s = "A9"
print(s.title().center(50, "-"))


def repeat_char(mystr1, mystr2):
    return mystr1 * int(mystr2)


print(repeat_char("pokemon", "2"))


# [Q10] Write a function that takes a list of numbers as input and returns a new list with all duplicates removed
s = "A10"
print(s.title().center(50, "-"))


def remove_duplicates(mylist):
    newlist = []
    for i in mylist:
        if i not in newlist:
            newlist.append(i)
    return newlist


print(remove_duplicates([1, 2, 3, 4, 3, 2, 8, 7, 1, 3, 5, 9, 8]))
