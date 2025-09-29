num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operatorq = input("Enter an operator (+,-,/,^,*): ")

if operatorq == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operatorq == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operatorq == "/":
    try:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    except ZeroDivisionError:
        print("num2 cannot be 0")
elif operatorq == "^":
    result = num1 ** num2
    print(f"{num1} ^ {num2} = {result}")
elif operatorq == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
else:

    print("Wrong operator input!!!")
