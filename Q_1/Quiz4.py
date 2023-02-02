#輸入兩個正數n,s，代表正n邊形之邊長為s
#計算並輸入此正n邊形之面積
import math #引用math模組

n = eval(input()) #設定3個輸入
s = eval(input()) #

Area = ( (n*math.pow(s,2)) / (4* math.tan(math.pi/n)) )
print('Area = %.4f' % Area)