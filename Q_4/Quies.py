n = eval(input())
lib = {}
num = int(0)
min = int(65536)

while (n == 9999):
    n = eval(input())
    num += 1
    lib[num] = n

for x in lib:
    for y in x:
        if (lib[x] > lib[y]):
            tmp = num[x];
            num[x] = num[y];
            num[x] = tmp;
        

min = lib[1]
print(min)