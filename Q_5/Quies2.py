import math

def compute(x,y,z):
    x1 = ((-1*y) * math.sqrt(math.pow(y,2) - (4 * x * z)) ) / (2 * x)
    x2 = ((-1*y) * (-1*math.sqrt(math.pow(y,2) - (4 * x * z))) ) / (2 * x)
    return x1,x2

a = eval(input())
b = eval(input())
c = eval(input())

print('%f, %f' % compute(a,b,c))