print("Sum of Numbers")

num = int(input("Enter number to calculate sum from 1 to number : "))
x = 0
for i in range(1,num):
    x = x + (i + 1)
    print(f"Sum of {x} and {i+1} is : {x}")
    

    