#假設一賽跑選手在x分y秒的時間跑完z公里，請撰寫一程式
#輸入x，y，z數值，最後顯示此選手每小時平均英哩速度

x = eval(input()) #設定3個輸入
y = eval(input()) #
z = eval(input()) #

Speed = (( ( (x*60) + y ) / 360 ) * z / 1.6 ) #將秒速換算成時速/英哩

print('Speed = %.1f' %  Speed) #輸出時速/英哩