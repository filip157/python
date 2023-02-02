#輸入一個半徑，並加給計算此圓之面積和周長
#最後請印出此圓的半徑(radius)，周長(Perimeter)和面積(Area)

import math #引用math模組

radius = eval(input()) #設定輸入半徑

print('Radius = %.2f' % radius)                #輸出該半徑和面積該半徑之周長和面積
print('Perimeter = %.2f' % (2*math.pi*radius)) #
print('Area = %.2f' % (math.pi*radius**2))     #