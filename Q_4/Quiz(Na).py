
n = 0
lib = []
min = 0
stop = 9999

while (n == stop):
    n = eval(input())
    lib = lib + [n]

for x in range(len(lib)):
    if (min > lib[x]):
        min = lib[x]

print(min)