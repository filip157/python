#輸入兩個正整數a,b(a<b)，利用迴圈計算從a開始的偶數連加到b的總和
#如:輸入 a = 1， b = 100，則輸出結果為2550(2+4+...+100=2550)

a = eval(input()) #設定2個輸入
b = eval(input()) #

c = 0

for x in range(a,b+1): #連加並放到c
    if (x % 2 == 0):
        c += x
print(c)