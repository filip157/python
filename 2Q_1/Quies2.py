card = []
tmp = []
time = 0
num = []

for time in range(10):
    card = card + [eval(input())]

print(card)

for time in range(10):
    num = card[time]|card
    tmpnum = 0
    #for time1 in range(10):
     #   if card[time] == card[time1]:
      #      num = num + [card[time]]
       #     tmpnum += 1
    print(num[0])
    print(len(num))

