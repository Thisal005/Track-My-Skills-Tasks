f = open("hello.txt", "r")
content = f.read()
f.close()


print(content)

with open("hello.txt", "a") as f:
    f.write("Hello putha")

with open("hello.txt","r") as f:
    print(f.read())

