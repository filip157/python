#

even = []
odd = []

for x in range(10):
    n = eval(input())
    if n % 2 == 0:
        even = even + [n]
    else:
        odd = odd + []
print('Even number:',len(even))
print('odd number:',len(odd))