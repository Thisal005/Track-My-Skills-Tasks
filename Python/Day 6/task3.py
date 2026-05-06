#Check your word is palindrome or not

word = input("Enter your word : ")
fwords = list(word)

bwords = list(word[-1::-1])


if fwords == bwords:
    print(f"{word} is a palindrome")
    #print(f"reverse of the enterd word is {word[-1::-1]}")
else:
    print(f"{word} is not a palindrome")



