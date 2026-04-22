num1 = input("Enter number one : ")
num2 = input("Enter number two : ")
num3 = input("Enter number three : ")

max = 0

if num1 > num2 :
    max = num1
    if num1 > num3:
        max = num1
    else:
        max = num3
elif num2 > num3:
    max = num2
elif num1 == num2 == num3:
    print("All 3 values are equal")
    max = num1
    pass
else:
    max = num3

print(f"The max number of {num1} , {num2} , {num3} is {max}")