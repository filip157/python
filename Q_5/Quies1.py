import math

def compute(x,y):
    pow = math.pow(x,y)
    return pow

a = eval(input())
b = eval(input())

print('%d' % compute(a,b))