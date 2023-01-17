a = eval(input())
b = eval(input())
c = int(0)

for x in range(a,b+1):
    if (x % 2 == 0):
        c += x
print(c)