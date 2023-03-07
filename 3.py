N = int(input("Enter the value of N: "))

# create an empty list to store the numbers
even_numbers = []

# loop through the first N even natural numbers and add them to the list
for i in range(2, (N+1)*2, 2):
    even_numbers.append(i)

# print the list of even numbers
print(even_numbers)
