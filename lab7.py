# Assignment 7
# David Cardona
# November 7, 2024

import turtle
import math  # Import math for calculating the area of a circle

def areaOfCircle(r):
    """Return the area of a circle with radius r"""
    return math.pi * (r ** 2)

def check_number(n, arr):
    """Return True if n is in arr; otherwise, return False"""
    return n in arr

def list_multiplication(arr):
    """Return the product of all elements in arr"""
    result = 1
    for num in arr:
        result *= num
    return result

def list_multiplication_recursive(arr):
    """Return the product of all elements in arr using recursion"""
    if len(arr) == 0:
        return 1
    else:
        return arr[0] * list_multiplication_recursive(arr[1:])

def get_unique(arr):
    """Return a list with only unique elements of arr"""
    return list(set(arr))

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""
    for _ in range(4):
        t.forward(sz)
        t.left(90)

def main():
    # Testing the functions
    r = 3
    n = 9
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr_with_duplicates = [1, 2, 3, 2, 4, 3, 5]

    # Test areaOfCircle
    print(f"Area of circle with radius {r}: {areaOfCircle(r)}")

    # Test check_number
    print(f"Is {n} in the list? {check_number(n, arr)}")

    # Test list_multiplication
    print(f"Multiplication of all elements in {arr}: {list_multiplication(arr)}")

    # Test list_multiplication_recursive (extra credit)
    print(f"Multiplication of all elements in {arr} using recursion: {list_multiplication_recursive(arr)}")

    # Test get_unique
    print(f"Unique elements in {arr_with_duplicates}: {get_unique(arr_with_duplicates)}")

    # Test drawSquare
    wn = turtle.Screen()
    alex = turtle.Turtle()
    alex.color("blue")
    drawSquare(alex, 100)
    wn.exitonclick()

if __name__ == "__main__":
    main()
