import math


input("Enter the coefficients for ax^2 + bx + c = 0")
a = float(input("Please enter the number a: "))
b = float(input("Please enter the number b: "))
c = float(input("Please enter the number c: "))



def OperationSpicyWater(a, b, c):
    
    d = b**2-4*a*c

    if d < 0:
        return "Invalid"

    elif d == 0:
        x = (-b+math.sqrt(b**2-4*a*c))/2*a
        return "This equation has one solution, and it is: ", x
    else:
        x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
        x2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
        return "There are two solutions: ", x1, " or", x2

OperationSpicyWater(a, b, c)

returnedResult = OperationSpicyWater(a, b, c)
print(returnedResult)
