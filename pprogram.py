"""
Suppose a list has 20 numbers. Write a program that removes all duplicates from this list.


"""
import random

# Step 1: Generate a list of 20 random integers between 1 and 10
random_list = [random.randint(1, 10) for _ in range(20)]
print("Random List:", random_list)

# Step 2: Remove duplicates from the list
unique_list = list(set(random_list))

# Step 3: Print the list without duplicates
print("List without duplicates:", unique_list)
