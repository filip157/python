#輸入一個正整數n，利用迴圈計算並輸出n!的值

n = eval(input()) #設定1個輸入

sum = 1

for x in range(1,n): #迴圈計算n!值
    sum += sum*(n-x);
    
print(sum)