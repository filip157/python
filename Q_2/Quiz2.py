#根據使用這輸入的分數顯示對應的等級

a = eval(input()) #設定1個輸入

if (a < 100 & a >= 80): #判斷分數對應的等級
    print('A')
elif (a < 79 & a >= 70):
    print('B')
elif (a < 69 & a >= 60):
    print('C')
elif (a <= 59):
    print('F')