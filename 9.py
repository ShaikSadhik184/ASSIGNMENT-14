my_list = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 5]
element = 1

indices = [i for i in range(len(my_list)) if my_list[i] == element]

print(f"The element {element} appears at indices: {indices}")
