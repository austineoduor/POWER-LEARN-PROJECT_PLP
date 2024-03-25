#!/usr/bin/python3


operation = {"A":"add","B":"sub","C":"mult","D":"div",}

print("\nchoose operation -: ")
for i, v in operation.items():
    print(f"{i} : {v}")

choice = str(input("Input your choice?  ")).upper()

num_1 = int(input("\nInput first number here.. "))
num_2 = int(input("Input second number here.."))
print("\n")

if num_1 != None and num_1 != None:
    match choice:
        case "A":
            result = num_1 + num_2
            print(f"Result of {num_1} + {num_2} is: {result}")
        case "B":
            result = num_1 - num_2
            print(f"Result of {num_1} - {num_2} is: {result}")
        case "C":
            result = num_1 + num_2
            print(f"Result of {num_1} * {num_2} is: {result}")
        case "D":
            result = float(num_1/num_2)
            print(f"Result of {num_1} / {num_2} is: {result}")
        case _:
            print("Ivalid choice")

