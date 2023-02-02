#輸入一個正整數，然後判斷他是3或5的倍數，若此數值同時為3與5的倍數
#顯示[x is a multiple of 3 and 5']:如此數值皆不屬於3或5的倍數，顯示[x is not a multiple of 3 or 5]

x = eval(input()) #設定1個輸入

if ((x % 3 == 0) & (x % 5 == 0)): #判斷是否是3與5的倍數
    print('x is a multiple of 3 and 5')
elif (x % 3 == 0): #判斷是否是3的倍數
    print('x is a multiple of 3')
elif (x % 5 == 0): #判斷是否是5的倍數
    print('x is a multiple of 5')
else : #不是3與5的倍數則輸出
    print('x is not a multiple of 3 or 5')