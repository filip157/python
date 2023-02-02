import math

n = eval(input())
sum = float( 1 / (1+(math.sqrt(2))) )

for x in range(3,n+1):
    sum +=1/(math.sqrt(x-1)+math.sqrt(x))

print('%.4f' % sum)