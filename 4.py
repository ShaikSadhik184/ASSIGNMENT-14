numbers = [5, 3, 8, 1, 9, 2, 7]

# set the first number in the list as the initial maximum value
max_number = numbers[0]

# loop through the list of numbers and update the maximum value if a larger number is found
for num in numbers:
    if num > max_number:
        max_number = num

# print the maximum number
print("The greatest number in the list is:", max_number)
