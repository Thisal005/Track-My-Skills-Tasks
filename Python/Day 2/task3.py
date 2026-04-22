print("Grade calculator")
marks = int(input("Enter your marks : "))

if marks >= 75:
    print("Congraulations! your grade is A ")
elif marks < 75 and marks >= 65:
    print("Congraulations! your grade is B ")
elif marks < 65 and marks >= 55:
    print("Congraulations! your grade is C ")
elif marks < 55 and marks >= 35:
    print("Your grade is S ")
elif marks < 35 and marks >=0:
    print("Eww!, You are Faild F")
else:
    print("What the fk is you just enterd")