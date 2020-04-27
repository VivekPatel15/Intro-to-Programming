fileName = 'C:/Users/Vivek/Desktop/Programming/employee.txt'
print(fileName)

updateList = 'C:/Users/Vivek/Desktop/Programming/employeeUpdate.txt'

outfile = open(updateList, 'w')

fileHandle = open(fileName, 'r')

for line in fileHandle:

    updatedLine = line.strip()
    employee = updatedLine.split(' ')
    salary = float(employee[2].strip())
    rate = float(employee[3].strip())/100

    increase = salary * rate
    salaryUpdate = increase + salary

    last = employee[0].strip()
    first = employee[1].strip()

    print('{:<15s} {:<15s} {:.2f} {:.2f} {:.2f}'.format(first, last, salary, salaryUpdate, increase))

    outfile.write('{:<15s} {:<15s} {:.2f} {:.2f} {:.2f} \n'.format(first, last, salary, salaryUpdate, increase))
outfile.close()
