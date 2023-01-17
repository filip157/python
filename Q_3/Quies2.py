n = eval(input())
sum = int(1)

for x in range(1,n):
    sum += sum*(n-x);
    
print(sum)