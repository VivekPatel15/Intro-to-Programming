populationA = int(input('Emter the population of Town A: '))
growthRateA = float(input('Enter the % growth rate of Town A: '))/100
populationB = int(input('Emter the population of Town B: '))
growthRateB = float(input('Enter the % growth rate of Town B: '))/100
year = 0

while populationA < populationB:
    populationA += (populationA * growthRateA)
    populationB += (populationB * growthRateB)
    year += 1

    if populationA >= populationB:
        print('Town A will grow larger than Town B in ' + str(year) + ' years.')
        print('Town A will have ' + str(int(populationA)) + ' inhabitants, while Town B will have ' + str(int(populationB)) + ' inhabitants.')
        break
