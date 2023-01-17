import math

n = eval(input())
s = eval(input())

Area = ( (n*math.pow(s,2)) / (4* math.tan(math.pi/n)) )
print('Area = %.4f' % Area)