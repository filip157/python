#輸入一個數字，此數字代表後面測試資料的數量，每一筆測試資料是一個正整數(由使用者輸入)，將此正整數的每位數全部加總起來

a = int(input()) #設定1個輸入

sum = 0 #設定加總

for i in range(a): #執行設定次數迴圈
    
    n = str(input()) #設定數字輸入
    time = len(n) #判斷數字長度

    for x in range(time):
        sum = sum + int(n[x])

    print('Sum of all digits of ',n,'is',sum)
    sum = 0