#輸入一個十進位整數num(0<=num<=15)，將num轉換成十六進位值

num = eval(input()) #設定輸入

if (num >= 10): #如果超過十進位，判斷十六進位值
    if (num == 10):
        print('A')
    elif (num == 11):
        print('B')
    elif (num == 12):
        print('C')
    elif (num == 13):
        print('D')
    elif (num == 14):
        print('E')
    elif (num == 15):
        print('F')
else:
    print(num)