money = input('Enter how much money you will play with: ')

pot = float(money)

maxPot = pot
rolls = 0

import random

while pot > 0:
    rollA = (random.randrange(1,6))
    rollB = (random.randrange(1,6))
    rolls += 1

    if rollA + rollB == 7:
        pot += 4
        if pot > maxPot:
            maxPot = pot
    else:
        pot -= 1

    if pot <= 0:
        print('You lasted ' + str(rolls) + ' rolls.')
        print('Your max pot was $' + str(maxPot) + '.')
        break

    
