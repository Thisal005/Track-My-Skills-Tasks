Numbers = [20, 5, 41, 85, 6, 2, 55, 73, 21, 10, 9, 12, 3, 4, 5, 6, 7, 8, 9, 10, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]

newNumbers = list(Numbers)
x = 0
y = 0
maxN = 0
minN = 1000



while True:
    newNumbers.sort()
    min = newNumbers[0]
    max = newNumbers[len(newNumbers) - 1 ]
    print(f"Smallest number in {Numbers} is {min} and the largest number is {max}")
    break

for i in range(len(Numbers)):
    if Numbers[i] > maxN:
        maxN = Numbers[i]
        #minN = maxN
    if Numbers[i] < minN:
        minN = Numbers[i]
    
print(f"Max numbers is {maxN}")
print(f"Min number is {minN}")