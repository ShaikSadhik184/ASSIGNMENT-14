my_list = [1, 2, 3, 1, 2, 3, 4, 5, 6, 5, 4, 7, 8, 7, 9, 10]

distinct_list = list(set(my_list))

for i in distinct_list:
    count = my_list.count(i)
    print(f"{i} occurs {count} times in the list.")
