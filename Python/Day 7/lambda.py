# Practice lambda function in python

# A lambda function that adds 10 to the input argument

x = lambda a : a + 10
print(x(5))

# A lambda function that add two numbers
y = lambda a, b : a + b
print(y(5,6))


# A lambda function that use filter to identify odd numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)