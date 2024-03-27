#!/usr/bin/python3

result = 0

def large_power(base, exponent):
    '''calculate power and return the result
    takes two arguments:
        base
        exponent
        return base raised to exponent

    '''
    result = base**exponent
    if result > 5000:
        return True
    return False

if __name__ == '__main__':
    try:
        a = int(input("input the Base "))
        b = int(input("input the exponent "))
    except ValueError:
        print("input numbers only please ")
    print(large_power(a, b))
