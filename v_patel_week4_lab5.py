money = input('Enter how much money you will play with: ')

pot = float(money)

maxPot = pot
rolls = 0

import random

if pot < 1:
    print('You need at least $1 to play this game.')

else:

    while pot >= 1:
        rollA = (random.randrange(1,6))
        rollB = (random.randrange(1,6))
        rolls += 1

        if rollA + rollB == 7:
            pot += 4
            if pot > maxPot:
                maxPot = pot
        else:
            pot -= 1

        if pot < 1:
            print('You ran out of money at ' + str(rolls) + ' rolls.')
            print('Your max pot was $' + str(maxPot) + '.')
            break
