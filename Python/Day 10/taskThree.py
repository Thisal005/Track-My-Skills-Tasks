with open("python.txt", "r") as f :
    content = f.read().lower()

word = input("Enter word to search in this file : ").lower()
count = content.count(word)

print(f"{word} appears in {count} times in this file")


with open("python2.txt", "w") as f:
    f.write(content)