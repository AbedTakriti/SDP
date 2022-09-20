from math import sqrt
from random import random

import Task3
from Task1 import *
from Task2 import *
import Task3
from Task4 import *
from Task3 import print_rank



@Decorator1
@Decorator2
@decorator3
@Decorator4

def Quad(a, b, c):
    """This function solve quadractic equations"""
    delta = b ** 2 - 4 * a * c
    root1 = (-b + sqrt(delta)) / (a * 2)
    root2 = (-b - sqrt(delta)) / (a * 2)
    return root1, root2
@Decorator1
@Decorator2
@decorator3
@Decorator4

def Pascal(n):
    """This function prints out Pascal pyramids of n rows"""
    trow = [1]
    y = [0]
    for x in range(max(n, 0)):
        print(" "*(n-x),end="")
        print (trow)
        trow = [l + r for l, r in zip(trow + y, y + trow)]
    return n >= 1

@Decorator1
@Decorator2
@decorator3
@Decorator4

def print_rand():
    """this function prints out  random numbers"""
    w= lambda x:print(x)
    print(random()

@Decorator1
@Decorator2
@decorator3
@Decorator4
def filter_less10(*args):
    """It filters out any element that is less than 10"""
    return list(filter(lambda value: value >10, args))

if __name__ == "__main__":
    #print_rand()
    filter_less10(12,3,4,5,6543,321,654)
    Quad(1,-2,-2)
    Pascal(10)
    Quad(1, -2, -2)
    print_rank()