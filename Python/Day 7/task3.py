# Calculator

def calculator(a,b,c):
    if(c == "+"):
        answer = a + b
        print(f"The  sum of {a} + {b} = {answer}")
    elif(c == "-"):
        answer = a - b
        print(f"The substraction of {a} - {b} = {answer}")
    elif(c == "*"):
        answer = a * b
        print(f"The multiplication of {a} * {b} = {answer}")
    elif(c == "/"):
        answer = a / b
        print(f"The division of {a} / {b} = {answer}")
    else:
        print("Invalid Operator!")

num1 = float(input("Enter number one : "))
num2 = float(input("Enter number two : "))
op = input("Enter operator ( +, -, *, /) : ")

while True:
    choice = input("To continue calculation press c : ")
    if choice == 'c':
        num1 = float(input("Enter number one : "))
        num2 = float(input("Enter number two : "))
        op = input("Enter operator ( +, -, *, /) : ")
        calculator(num1,num2,op)
    else:
        break
