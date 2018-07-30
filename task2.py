import random

words = [word.rstrip('\n') for word in open('words.txt')]
randomPhrase = " ".join([words[random.randrange(0, len(words))] for i in range(4)])

print(randomPhrase)

#reverse words and letters in randonPhrase
reversePhrase = randomPhrase[::-1]

print(reversePhrase)
