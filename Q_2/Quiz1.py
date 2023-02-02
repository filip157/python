#輸入兩個整數a,b，然後再輸入一運算子(+，-，*，/，//，%)
#輸出這兩個數以及其經過運算的結果

a = eval(input()) #設定2個輸入
b = eval(input()) #

c = input() #設定運算子輸入

if (c == '+'): #判斷哪種運算子
    print(a+b)
elif (c == '-'):
    print(a-b)
elif (c == '*'):
    print(a*b)
elif (c == '/'):
    print(a/b)
elif (c == '//'):
    print(a//b)
elif (c == '%'):
    print(a%b)