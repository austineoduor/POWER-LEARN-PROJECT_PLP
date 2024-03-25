#!/usr/bin/python3

my_list = []
lst = [10, 20, 30, 40]
lst1 = [50, 60, 70]
for i in lst:
    my_list.append(i)
my_list.insert(1, 15)
my_list.extend(lst1)
my_list.pop()
my_list.sort()
for i in range(len(my_list)):
    if my_list[i]== 30:
        print(f"30 is at index {i}")
