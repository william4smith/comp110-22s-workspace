"""Chardle exercise"""

__author__ = "730467449"


word: str = input("Enter a 5-character word: ")
if len(word) < 5:
    print("Error: Word must contain 5 characters")
    exit()

if len(word) > 5:
    print("Error: Word must contain 5 characters")
    exit()


letter: str = input("Enter a single character: ")
if len(letter) < 1:
    print("Error: Character must be a single character.")
    exit()

if len(letter) > 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + letter + " in " + word)


if word[0] == letter:
    print(letter + " found at index 0")

if word[1] == letter:
    print(letter + " found at index 1")

if word[2] == letter:
    print(letter + " found at index 2")

if word[3] == letter:
    print(letter + " found at index 3")

if word[4] == letter:
    print(letter + " found at index 4")


string = word
substring = letter
counting: str = string.count(substring)


if counting == 0:
    print("No instances of " + letter + " found in " + word)

if counting == 1:
    print("1 instance of " + letter + " found in " + word)

if counting == 2:
    print("2 instances of " + letter + " found in " + word)

if counting == 3:
    print("3 instances of " + letter + " found in " + word)

if counting == 4:
    print("4 instances of " + letter + " found in " + word)

if counting == 5:
    print("5 instances of " + letter + " found in " + word)