x = eval(input())
y = eval(input())
z = eval(input())

if (y+z >= x):
    if (x+z >= y):
        if (x+y >= z):
            print(x+y+z)
        elif (z == x & x == y):
            print(x+y+z)
        else :
            print('Invalid')
else :
    print('Invalid')