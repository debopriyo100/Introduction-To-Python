lines = ["the car is grey ", "the mango is orange"]
words = []
for line in lines:
    for word in line.split():
        if len(word) > 2 and word != "the":
            words.append(word.upper())
print(words)