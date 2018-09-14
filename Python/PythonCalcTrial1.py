def DoMath():
    math = input('What kind of equation do you want:  ')
    if math == '+':
        number1 = input("please Enter the First Number: ")
        number2 = input("please Enter the Second Number: ")

        sum = round(float(number1) + float(number2), 2)
        print('the sum of {0} and {1} is {2}'.format(number1,number2,sum))

    if math == '-':
        number1 = input("please Enter the First Number: ")
        number2 = input("please Enter the Second Number: ")

        sum = round(float(number1) - float(number2), 2)
        print('the diffrence of {0} and {1} is {2}'.format(number1,number2,sum))

    if math == '*':
        number1 = input("please Enter the First Number: ")
        number2 = input("please Enter the Second Number: ")

        sum = round(float(number1) * float(number2), 2)
        print('the multiple of {0} and {1} is {2}'.format(number1,number2,sum))

    if math == '/':
        number1 = input("please Enter the First Number: ")
        number2 = input("please Enter the Second Number: ")

        sum = round(float(number1) / float(number2), 2)
        print('the quotient of {0} and {1} is {2}'.format(number1,number2,sum))

    if math == '%':
        number1 = input("please Enter the First Number: ")
        number2 = input("please Enter the Second Number: ")

        sum = round(float(number1) % float(number2), 2)
        print('the modulo of {0} and {1} is {2}'.format(number1,number2,sum))


