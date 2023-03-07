my_list = [1, 'apple', 3.5, 'banana', 5, 'orange', 6.7, 8]

my_list = [x for x in my_list if isinstance(x, int)]

print(my_list)
