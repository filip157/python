#輸入四個數字x1,y1,x2,y2，分別代表兩個點的座標(x1,y1)，(x2,y2)
#計算這兩個點的座標與其歐式距離

import math #引用math模組

x1 = eval(input()) #設定4個輸入
y1 = eval(input()) #
x2 = eval(input()) #
y2 = eval(input()) #

O = math.sqrt( math.pow((x1-x2),2) + math.pow((y1-y2),2) )
print('(' ,  x1 , ',' , y1 , ')')
print('(' ,  x2 , ',' , y2 , ')')
print('Distance = ' , O)