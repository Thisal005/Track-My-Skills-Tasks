print("Basic Calculator")

num1 = float(input("Enter number one : "))
num2 = float(input("Enter number two : "))
operator = input("Enter operator ( +, -, *, /) : ")

if(operator == "+"):
    answer = num1 + num2
    print(f"The  sum of {num1} + {num2} = {answer}")
elif(operator == "-"):
    answer = num1 - num2
    print(f"The substraction of {num1} - {num2} = {answer}")
elif(operator == "*"):
    answer = num1 * num2
    print(f"The multiplication of {num1} * {num2} = {answer}")
elif(operator == "/"):
    answer = num1 / num2
    print(f"The division of {num1} / {num2} = {answer}")
else:
    print("Invalid operator!")