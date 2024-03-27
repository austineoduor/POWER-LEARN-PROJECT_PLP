#!/usr/bin/python3

def calculate_discount(price, discount_percent):
    """
    take price and discount percentage as argument and return
    price with discount if applicable only above 20% or higher
    """
    if discount_percent >= 20:
        price = price - (price * 20/100)
        return price
    return price

if __name__ == '__main__':
    try:
        price = int(input("Input product orginal price "))
        dis = int(input("Input discount for the product "))
    except ValueError:
        print("Numbers only pleas")
    res = calculate_discount(price, dis)

    print("\nThe product price is {}".format(res))
