# Advanced Problem Set: Delving Deeper with Numbers in Python

#################### PROBLEM 1: Basic Arithmetic & Order of Operations ####################
# Task 1: Using the order of operations (PEMDAS/BODMAS), evaluate the following expression:
# 3 + 6 * (5 + 4) / 3 - 7. Print the result.
mathematics = 3 + 6 * ( 5 + 4 ) / 3 -7
print(mathematics)
# Task 2: Calculate the remainder when 145 is divided by 12 using modulo and print the result.
mather2 = 145%12
print(mather2)

# Task 3: Raise 7 to the power of 3 and print the result.
powermath = 7 ** 3
print(powermath)

#################### PROBLEM 2: Working with Functions ####################
# Task 4: Given a list of numbers:
numbers = [23, 89, 12, 54, 92, 65, 71, 13, 45]
# Use the max() and min() functions to find the highest and lowest number respectively.
print(max(numbers))
print(min(numbers))

# Task 5: Round the number 12.5678 to 2 decimal places.
print(round(12.5678,2))

# Task 6: Find the absolute value of -45.
print(abs(-45))

#################### PROBLEM 3: Advanced Math Functions ####################
import math
from math import *

# Task 7: Using the math library, find the floor value of 15.7.
print(math.floor(15.7))

# Task 8: Find the ceiling value of 15.2.
print(math.ceil(15.2))

# Task 9: Calculate the square root of 625.
print(math.sqrt(625))

#################### PROBLEM 4: Problem Solving ####################
# Task 10: You are given two lists:
prices = [34.56, 45.78, 23.89, 12.34, 78.90]
quantities = [3, 5, 2, 4, 6]
# Calculate the total cost for each item (price multiplied by quantity).
mather10 = 34.56 * 3
mather11 = 45.78 * 5
mather12 = 23.98 * 2
mather13 = 12.34 * 4
mather14 = 78.90 * 6
print(sum(prices))
print(sum(quantities))
print(sum(prices) * sum(quantities))
total_cost = [mather10, mather11, mather12, mather13, mather14]
print(total_cost)
# Then, find the average cost of all items after rounding it to 2 decimal places.
average_cost = round(sum(total_cost) / len(total_cost), 2)
print(average_cost)
print(round(mather10,2))
print(round(mather11,2))
print(round(mather12,2))
print(round(mather13,2))
print(round(mather14,2))
averagemath = (103.68 + 228.9 + 47.96 + 49.36 + 473.4) / 5
print(averagemath)
#################### END OF ADVANCED PROBLEM SET ####################
