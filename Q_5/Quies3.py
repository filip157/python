import math


def compute(x,y):
    while(y != 0):
        tmp = x % y; 
        x = y; 
        y = tmp; 
    return x

a = eval(input())
b = eval(input())

print(compute(a,b))