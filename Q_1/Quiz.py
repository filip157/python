#輸入四個分別含有小數1到4位的浮點數，然後將這四個浮點數以欄寬為7
#每列印兩個的方式，先列印向右靠齊，再列印向左靠齊，左右皆以直線(Vertical bar)|作為邊界

a = eval(input()) #設定4個輸入
b = eval(input()) #
c = eval(input()) #
d = eval(input()) #

print('|% .2f' % a , '  ' , '% .2f|' % b) #輸出所需方式
print('|% .2f' % c , '  ' , '% .2f|' % d) #
print('|%-.2f' % a , '  ' , '%-.2f|' % b) #
print('|%-.2f' % c , '  ' , '%-.2f|' % d) #