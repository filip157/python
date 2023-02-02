card = []
times = []
position = 0

for time in range(10):
    card = card + [eval(input())]
    if (card[time] not in times):
        times[time] = 1
    elif (card[time] in times):

    else:
        eos = 0
print(card)

for time in range(10):
    tmpnum = 0
    num = []
    for time1 in range(10):
        if card[time] == card[time1]:
                tmpnum += 1
    print(num[0])
    print(len(num))