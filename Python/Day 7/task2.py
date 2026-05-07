# check the number is prime or not

num = int(input("Enter number to check prime or not : "))

def prime(n):
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:    print(f"{num} is a prime number")  

prime(num)