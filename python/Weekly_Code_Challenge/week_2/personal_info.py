#!/usr/bin/python3

dict1 = {}
Name = str(input("Please input your name "))
Age = int(input("Please input yuor age "))
Favorite_Color = str(input("Please input your favorite color "))

dict1["Name"] = Name
dict1["Age"] = Age
dict1["Favorite_Color"] = Favorite_Color

if dict1 is not None:
    for i, v in dict1.items():
        print(i, ":", v)
