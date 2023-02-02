#輸入一個正整數a，利用迴圈計算從1到a之間，從1到a之間，所有5之倍數數字總和

a = eval(input()) #設定1個輸入

b = 0

for x in range(1,a): #判斷是否為5的倍數並相加
    if (x % 5 == 0):
        b += x
print(b)