# Explore the empty string ("") and call string methods like upper, lower, title, rstrip, and lstrip on
# strings using dot notation. Find other string methods by typing the string and the dot in Pycharm and
# examining the drop-down menu. Call these methods on values ("literals") like "LAura".lower() and on
# variables (that have values assigned), e.g. first_name.lower().

my_string = "this is the title of a book now!"
print(my_string.upper())
print(my_string.lower())
print(my_string.title())

xbox = "\n\n\t\t\t\tThis is my string!\n\n\n\n"
print(xbox.lstrip())
print(xbox.rstrip())
# print(xbox.lstrip().rstrip())
print(xbox.strip())

# Work along with your PAL to import the libraries math and random and use them
import math
print(math.sqrt(25))
print(math.pi)

import random
print(random.randint(1, 10))


# 22.75*(1 + 0.15)

# Assign 1 as the value for the variable a, 2 for the value for the variable b, and -1 for the variable c.
# Calculate b^2 - 4ac by hand. Now use Python to check your answer.

a = 1
b = 2
c = -1

print(b**2 - 4 * a * c)

# Assign 0 as the value for the variable a. Explain what it means to change the value of a from the previous
# problem, given that a variable references a value. (It is a label for a value.)

a = 0
print(b**2 - 4 * a * c)

# What is the remainder when any even number is divided by 2? Illustrate your answer in Python using the
# remainder operator (also known as the modulus or mod operator) in various examples
print()
print(8 % 2)
print(10 % 2)
print(12 % 2)
print(14 % 2)
print(16 % 2)
print()
print(11 % 2)
print(17 % 2)
print(21 % 2)
print(35 % 2)


# 0.2 + 0.1
#  3 * 0.1
print(0.1 + 0.2) # = 0.30000000000000004
print(3 * 0.1) # = 0.30000000000000004


# Suppose a person purchases three lemons, three limes, and six oranges. Store the number of each fruit in a
# variable with a descriptive name using appropriate Python style.

num_of_oranges = 6
num_of_limes = 3
num_of_lemons = 3
