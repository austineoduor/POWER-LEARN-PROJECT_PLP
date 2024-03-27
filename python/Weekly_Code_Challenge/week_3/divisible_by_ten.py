#!/usr/bin/python3

def divisible_by_ten(num):
    '''
    check if a number is divisible by ten and returns
    true if the number is divisible by ten
    false otherwise
    '''
    if num % 10 == 0:
        return True
    return False

if __name__ == '__main__':
    try:
        a = int(input("Input a number "))
    except ValueError:
        print("Only numbers")
    print(divisible_by_ten(a))
