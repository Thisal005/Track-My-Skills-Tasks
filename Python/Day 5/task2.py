x = input("Enter a sentence to count the number of words: ")
word_count = len(x.split())
words = list(x.split())
print(words)

word_count = {}

for x in words:
    if x in word_count:
        word_count[x] += 1
    else:
        word_count[x] = 1

print(word_count)