# Word count in a sentence

sentence = input("Please Enter your sentence to count thenumber of words : ")
words = list(sentence.split(" " or "\t" or "\n" or "," or "." or "!" or "?" or ";" or ":" or "-" or "_" or "/" or "\\"))
count = len(words)

print(f"There are {count} words in the sentence")
