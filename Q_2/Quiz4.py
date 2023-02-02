#輸入三個邊長，檢查這三邊是否可以組成一個三角形
#可以，則輸入該三角形之周長:否則顯示[Invalid]

x = eval(input()) #設定3個輸入
y = eval(input()) #
z = eval(input()) #

if ((y+z >= x) | (x+z >= y) | (x+y >= z)): #判斷是否能組成三角形
    print(x+y+z)
else : #非三角形輸出
    print('Invalid')