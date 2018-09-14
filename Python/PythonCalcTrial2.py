NumberOne = float(input("Put Thine Number "))
NumberTwo = float(input("Put Thine Second Number "))
Equation = input("Put Thine Equation Symbol ")

def doMaths(a, b, c):
    if c == "+":
        return round(a + b, 2)
    if c == "-":
        return round(a - b, 2)
    if c == "*":
        return round(a * b, 2)
    if c == "/":
        return round(a / b, 2)
    if c == "%":
        return round(a % b, 2)
    
returnedResult = doMaths(NumberOne, NumberTwo, Equation)
print(returnedResult)
