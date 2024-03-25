#!/usr/bin/python3

lst = ["hello","world","plp","peer","eat",
         "walk","jump","run","scream","yawn","river"]
lst_1 = [item for item in lst if (len(item) % 2 != 0)]
print("Original list")
print(lst,"\n")
print("New list with odd number of characters")

print(lst_1)

