# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression


def linearSearch(anList, item):
    for n in anList:
        if n == item:
            return anList.index(n)
    return -1


def binarySearch(anList, item):
    li = 0
    ui = len(anList) - 1
    while ui >= li:
        mi = (li + ui) // 2
        if item == anList[mi]:
            return mi
        elif item < anList[mi]:
            ui = mi - 1
        else:
            li = mi + 1
    return -1


def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    # Print first 50 values of each list to verify contents
    print(dictionary[0:50])
    print(aliceWords[0:50])

    while True:
        print("\nMain Menu")
        print("1: Spell Check a Word (Linear Search)")
        print("2: Spell Check a Word (Binary Search)")
        print("3: Spell Check Alice In Wonderland (Linear Search)")
        print("4: Spell Check Alice in Wonderland (Binary Search)")
        print("5: Exit")
        selection = input("Enter menu selection (1-5): ")
        word_type = input("Please enter a word: ")

        if selection == "1":
            x = linearSearch(dictionary, word_type)
            print(x)
        elif selection == "2":
            y = binarySearch(aliceWords, word_type)
            print(y)
        elif selection == "3":
            w = linearSearch(aliceWords, word_type)
            print(w)
# end main()

# "python.terminal.executeInFileDir": true in preference settings from file checkmark


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
