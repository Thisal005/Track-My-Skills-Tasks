#First non repeating character in a string

s = input("Enter your string : ")
count = {}

characters = list(s.strip())
print(characters)

for x in characters:
    if x in count:
        count[x] += 1
    else:
        count[x] = 1

print(count)

c = ""

for x in count:
    if count[x] == 1:
        c = x
        break
print("First non repeating character is : ", c)

