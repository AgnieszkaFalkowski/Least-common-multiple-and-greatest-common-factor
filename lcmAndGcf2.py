choice = 'y'
greeting = "This program calculates the least common multiple and greatest common factor for two numbers of your choice."

def allFactors(x, y, xFactors, yFactors, commonFactors):
    for i in range(1, x+1):
        if x % i == 0:
            xFactors.append(i)
    for j in range(1, y+1):
        if y % j == 0:
            yFactors.append(j)
    commonFactors = [factor for factor in xFactors if factor in yFactors]
    print("Factors of ", x, ": ", xFactors)
    print("Factors of ", y, ": ", yFactors)
    print("Common factors: ", commonFactors)
    

def leastCommonMultiple(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater +=1
    return lcm

def greatestCommonFactor(x, y):
    while y:
        x,y = y, x%y
    return x

def allMultiples(x, y, xMultiples, yMultiples, commonMultiples):
    xMultiples = [x*k for k in range(1, y+1)]
    print("Multiples of ", x, ": ", xMultiples)
    yMultiples = [y*l for l in range(1, x+1)]
    print("Multiples of ", y, ": ", yMultiples)
    commonMultiples = [multiple for multiple in xMultiples if multiple in yMultiples]
    print("Common multiples: ", commonMultiples)
    
        
print(greeting)
while choice == 'y':
    
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    xFactors = []
    yFactors = []
    commonFactors = []
    xMultiples = []
    yMultiples = []
    commonMultiples = []

    allFactors(x, y, xFactors, yFactors, commonFactors)
    allMultiples(x, y, xFactors, yFactors, commonMultiples)
    lcm = leastCommonMultiple(x,y)
    gcf = greatestCommonFactor(x, y)
    print("Least common multiple: ", lcm)
    print("Greatest common factor: ", gcf)
    choice = input("Do you want to enter a different set of numbers? ( y or n):")
    if choice != 'y':
        print("Thank you for using the program. Have a great day!")
    
    
