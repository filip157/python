import math

time = int(0)

def compute(x):
    for time in x:
        if (time == 0):
            print('0')
        elif(time == 1):
            print('1')
            tmp1 = 0
            tmp2 = 0
        else:
            tmp1 = int(x)
            tmp2 = tmp1
            tmp = tmp1 + tmp2
            print('%d' % tmp)
    return

a = eval(input())

compute(a)