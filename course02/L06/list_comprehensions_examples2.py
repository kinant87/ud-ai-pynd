# Find all of the numbers from 1-1000 that are divisible by 7
print("Exercise 1:")

numbers = [num for num in range(1, 1001) if num % 7 == 0]
print(numbers)
print("")

# Find all of the numbers from 1-1000 that have a 3 in them
print("Exercise 2:")
numbers = [num for num in range(1, 1001) if str(num).count('3') > 0]
print(numbers)
print("")

# Count the number of spaces in a string
print("Exercise 3:")
test_string = ['This is just a test string that will be used to count spaces', 'And this is another string']
number_of_spaces = [tmp_string.count(' ') for tmp_string in test_string]
print(number_of_spaces)
print("")

# Create a list of all the consonants in the string “Yellow Yaks like yelling and yawning
# and yesturday they yodled while eating yuky yams”
print("Exercise 4:")
test_string = 'Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams'
consonants = [ch for ch in test_string if ch.lower() not in 'aeiou' and ch != ' ']
print(consonants)
print("")

# Get the index and the value as a tuple for items in the list “hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’).
# Result would look like (index, value), (index, value)
print("Exercise 5:")
sample_list = ['hi', 4, 8.99, 'apple', ('t, b', 'n')]
result = [(index, value) for index, value in enumerate(sample_list)]
print(result)
print("")

# Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5
print("Exercise 6:")
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
common_numbers = [list_a[i] for i in range(len(list_a)) if list_a[i] in list_b]
print(common_numbers)
print("")

# Get only the numbers in a sentence like ‘In 1984 there were 13 instances of a protest with over 1000 people attending’
print("Exercise 7:")
sample_text = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
only_numbers = [int(tmp_str) for tmp_str in sample_text.split() if tmp_str.isnumeric()]
print(only_numbers)
print("")

# Given numbers = range(20), produce a list containing the word ‘even’
# if a number in the numbers is even, and the word ‘odd’ if the number is odd.
# Result would look like ‘odd’,’odd’, ‘even’
print("Exercise 8:")
even_or_odd = ['even' if num % 2 == 0 else 'odd' for num in range(20)]
print(even_or_odd)
print("")

# Produce a list of tuples consisting of only the matching numbers in these
# lists list_a = 1, 2, 3,4,5,6,7,8,9, list_b = 2, 7, 1, 12. Result would look like (4,4), (12,12)
list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_b = [2, 7, 1, 12]
print("Exercise 9:")
#TODO
print("")

# Find all of the words in a string that are less than 4 letters
print("Exercise 10:")
print()
print("")

# Use a nested list comprehension to find all of the numbers from 1-1000 that
# are divisible by any single digit besides 1 (2-9)
print("Exercise 11: USING LOOPS")
test_list = []

for i in range(1, 100):
    for j in range(2, 10):
        print(f"i: {i}, j: {j}")
        if i % j == 0:
            test_list.append(i)
            break

print(list(set(test_list)))

print("Exercise 11: USING LIST COMPS")
# nested_list = list(set([i for i in range(1, 1001) for j in range(2, 10) if i % j == 0]))
nested_list = [[i for j in range(2, 10)] for i in range(100)]
print(nested_list)
print("")

# TESTING
print("TESTING AREA:")
fun = lambda x: x ** 2
test = [list(map(fun, [0, 1, 2, 3, 4])) for i in range(5)]
print(test)
