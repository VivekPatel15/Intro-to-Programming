center = input('Enter the center point of the circle as x,y (no parenthesis): ')
point = input('Enter a point of the circle as x,y (no parenthesis): ')

#center = (x1, y1)
#point = (x2, y2)

x1 = float(center.split(',')[0])
x2 = float(point.split(',')[0])
y1 = float(center.split(',')[1])
y2 = float(point.split(',')[1])

def radius(x1, y1, x2, y2):
    r = (((x2-x1)**2)+((y2-y1)**2))**(1/2)
    print("radius = " + str(r))

radius(x1, y1, x2, y2)
