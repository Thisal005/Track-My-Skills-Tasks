print("Vowels Counter!")

global vowels
vowels = 0

word = str(input("Enter your word : "))
for w in range(0, len(word)):
    if word[w] == "a" or word[w] == "e" or word[w] == "i" or word[w] == "o" or word[w] == "u":
        vowels += 1
        print("Vowel found")
print(f"Total number of vowels in {word} is {vowels}")