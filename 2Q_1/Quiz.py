card = []

def compute(x):
    if (x == 'K'):
        x = 13
    elif (x == 'k'):
        x = 13
    elif (x == 'Q'):
        x = 12
    elif (x == 'q'):
        x = 12
    elif (x == 'J'):
        x = 11
    elif (x == 'j'):
        x = 11
    else:
        x = int(x)
    return x 

for time in range(5):
    y = input()
    card = card + [compute(y)]

print(card)