# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression


def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    # Print first 50 values of each list to verify contents
    print(dictionary[0:50])
    print(aliceWords[0:50])
# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()


# Call main() to begin program
main()

while True:
    print("Main Menu")
    print("1: Spell Check a Word (Linear Search)")
    print("2: Spell Check Alice In Wonderland (Linear Search)")
    print("3: Spell Check Alice In Wonderland (Linear Search)")
    print("4: Spell Check Alice in Wonderland (Binary Search)")
    print("5: Exit")
    selection = input("Enter menu selection (1-5): ")
    input("")