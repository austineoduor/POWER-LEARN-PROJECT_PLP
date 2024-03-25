#!/bin/usr/python3

set1 = set()
set2 = set()

n = int(input("How many integers do you want "))
print("\nInput random numbers btwn 0 - 9")
for i in range(2):
    print(f"list {i+1}")
    for j in range(0, n):
        x = int(input(f" element-{j+1}: "))
        if i == 0:
            set1.add(x)
        else:
            set2.add(x)
set3 = set1.intersection(set2)
print("\nNew common set is")
print(set3)
