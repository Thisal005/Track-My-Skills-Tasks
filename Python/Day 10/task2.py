with open("test.txt", "r")as f:
    content = f.read().lower()

print("Word Count in a file : ", len(content.split()))
print("Character Count in a file : ", len(content))

word = input("Enter the word you want to search : ").lower()

if word in content:
    print("Word is present in the file")
else:
    print("Word is not present in the file")