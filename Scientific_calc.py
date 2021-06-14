import  math

def add(x, y):
    return x+y

def sub(x, y):
    return x- y

def multiply(x, y):
    return x*y

def  divide(x, y):
    return x/y

def sqrt(x):
    result = math.sqrt(x)

def exp(x):
    return x ** 2

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

print("""

Choose a number for the following operations

1 - Addition(x,y)
2- Subtraction (x,y)
3- Multiply(x,y)
4- Divide (x,y)
5 - Squre(x)
6 - Squre- root (x)
7- sin (x)
8- cos (x)
9 - Tan(x)



""")
output = int(input("What operation do you wanr to parform ? "))

#calculator scrite

while output< 10:
    if output == 1:
        print("enter of parameters")
        a = int(input("enter of numbers x = "))
        b = int(input("enter of numbers y= "))
        res = add(a, b)
        print(res)

    elif output == 2:
        print("enter of parameters")
        a = int(input("enter of numbers x = "))
        b = int(input("enter of numbers y= "))
        res = sub(a, b)
        print(res)

    elif output == 3:
        print("enter of parameters")
        a = int(input("enter of numbers x = "))
        b = int(input("enter of numbers y= "))
        res = multiply(a, b)
        print(res)

    elif output == 4:
        print("enter of parameters")
        a = int(input("enter of numbers x = "))
        b = int(input("enter of numbers y= "))
        res = divide(a, b)
        print(res)
    
    elif output == 5:
        print("enter of parameters")
        a = int(input("enter of numbers x = "))
        b = int(input("enter of numbers y= "))
        res = sqrt(a, b)
        print(res)

    elif output == 6:
        print("enter of parameters")
        a = int(input("enter of numbers x = "))
        b = int(input("enter of numbers y= "))
        res = exp(a, b)
        print(res)

    elif output == 7:
        print("enter of parameters")
        a = int(input("enter of numbers x = "))
        b = int(input("enter of numbers y= "))
        res = sin(a, b)
        print(res)

    elif output ==8 :
        print("enter of parameters")
        a = int(input("enter of numbers x = "))
        b = int(input("enter of numbers y= "))
        res = cos(a, b)
        print(res)

    elif output == 9:
        print("enter of parameters")
        a = int(input("enter of numbers x = "))
        b = int(input("enter of numbers y= "))
        res = tan(a, b)
        print(res)

    else:
        print("Choose another function")

    new = int(input("do you want to  continue - (yes - 1) (no -2)"))
    
    if  new ==1 :
        output = int(input(" enter of operation"))

    elif new ==0 :
        print("Thanks for using the sciencetific calculator")
        break 








