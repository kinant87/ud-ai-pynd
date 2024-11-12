# These exercises are not part of the course materials, but I am having a hard time with more
# complex list comprehensions, so I decided to look for extra exercises online

# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())

# Exercise 1 - rewrite the above example code using list comprehension syntax.
# Make a variable named uppercased_fruits to hold the output of the list comprehension.
# Output should be ['MANGO', 'KIWI', etc...]
print("Exercise 1:")
uppercased_fruits = [fruit.upper() for fruit in fruits]
print(uppercased_fruits)
print("")

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce
# output like ['Mango', 'Kiwi', 'Strawberry', etc...]
print("Exercise 2:")
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print(capitalized_fruits)
print("")

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels.
# Hint: You'll need a way to check if something is a vowel.
print("Exercise 3:")


def num_vowel(word):
    count = 0

    for letter in word:
        if letter.lower() in 'aeiou':
            count += 1

    return count


fruits_with_more_than_two_vowels = [fruit for fruit in fruits if num_vowel(fruit) > 2]
print(fruits_with_more_than_two_vowels)
print("")

# Exercise 4 - make a variable named fruits_with_only_two_vowels.
# The result should be ['mango', 'kiwi', 'strawberry']
print("Exercise 4:")
fruits_with_only_two_vowels = [fruit for fruit in fruits if num_vowel(fruit) == 2]
print(fruits_with_only_two_vowels)
print("")

# Exercise 5 - make a list that contains each fruit with more than 5 characters
print("Exercise 5:")
fruits_more_5_chars = [fruit for fruit in fruits if len(fruit) > 5]
print(fruits_more_5_chars)
print("")

# Exercise 6 - make a list that contains each fruit with exactly 5 characters
print("Exercise 6:")
fruits_5_chars = [fruit for fruit in fruits if len(fruit) == 5]
print(fruits_5_chars)
print("")

# Exercise 7 - Make a list that contains fruits that have less than 5 characters
print("Exercise 7:")
fruits_less_5_chars = [fruit for fruit in fruits if len(fruit) < 5]
print(fruits_less_5_chars)
print("")

# Exercise 8 - Make a list containing the number of characters in each fruit.
# Output would be [5, 4, 10, etc... ]
print("Exercise 8:")
fruits_chars = [len(fruit) for fruit in fruits]
print(fruits_chars)
print("")

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of
# only the fruits that contain the letter "a"
print("Exercise 9:")
fruits_with_a = [fruit for fruit in fruits if fruit.count('a') != 0]
print(fruits_with_a)
print("")

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers
print("Exercise 10:")
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)
print("")

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
print("Exercise 11:")
odd_numbers = [number for number in numbers if number % 2 != 0]
print(odd_numbers)
print("")

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
print("Exercise 12:")
positive_numbers = [number for number in numbers if number >= 0]
print(positive_numbers)
print("")

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
print("Exercise 13:")
negative_numbers = [number for number in numbers if number < 0]
print(negative_numbers)
print("")

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of
# numbers with 2 or more numerals
print("Exercise 14:")
numbers_2_numerals = [number for number in numbers if number >= 10]
print(numbers_2_numerals)
print("")

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list
# with each element squared. Output is [4, 9, 16, etc...]
print("Exercise 15:")
numbers_squared = [number ** 2 for number in numbers]
print(numbers_squared)
print("")

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the
# numbers that are both odd and negative.
print("Exercise 16:")
odd_negative_numbers = [number for number in numbers if number % 2 != 0 and number < 0]
print(odd_negative_numbers)
print("")

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five.
print("Exercise 17:")
numbers_plus_five = [(number + 5) for number in numbers]
print(numbers_plus_five)
print("")

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list.
# *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
print("Exercise 18:")


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


prime_numbers = [number for number in numbers if is_prime(number)]
print(prime_numbers)
print("")
