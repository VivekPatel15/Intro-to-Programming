C = int(input('Enter the length of longest side of the triangle: '))
A = int(input('Enter the length of one of the remaining sides: '))
B = int(input('Enter the length of the last remaining side: '))

if A**2 + B**2 == C**2:
    print('This is a right triangle.')
else:
    print('This is not a right triangle.')
