a = eval(input())
b = int(0)

for x in range(1,a):
    if (x % 5 == 0):
        b += x
print(b)