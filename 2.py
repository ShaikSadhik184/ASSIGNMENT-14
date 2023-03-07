N = int(input("Enter the value of N: "))

# create an empty list to store the numbers
odd_numbers = []

# loop through the first N odd natural numbers and add them to the list
for i in range(1, N*2, 2):
    odd_numbers.append(i)

# print the list of odd numbers
print(odd_numbers)
