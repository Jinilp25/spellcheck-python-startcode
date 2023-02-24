# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import time  # Needed for timing the search functions

# Linear Search Function


def linearSearch(anList, item):
    for i in range(len(anList)):
        if anList[i] == item:
            return i
    return -1

# Binary Search Function


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

    # While Loop
    while True:
        # Main Menu
        print("\nMain Menu")
        print("1: Spell Check a Word (Linear Search)")
        print("2: Spell Check a Word (Binary Search)")
        print("3: Spell Check Alice In Wonderland (Linear Search)")
        print("4: Spell Check Alice in Wonderland (Binary Search)")
        print("5: Exit")
        selection = input("Enter menu selection (1-5): ")
        # Print word type only if user selects option 1 or 2
        if selection == "1" or selection == "2":
            word_type = input("Please enter a word: ")

        # Print the position and time taken using linear Search
        if selection == "1":
            print("\nLinear Search Starting...")
            startTime = time.time()
            x = linearSearch(dictionary, word_type)
            endTime = time.time()
            time_elapsed = endTime - startTime
            if x == -1:
                print(word_type + " is NOT IN the dictionary. (" +
                      str(time_elapsed) + " seconds)")
            else:
                print(word_type + " is IN the dictionary at position " +
                      str(x) + ". (" + str(time_elapsed) + " seconds)")
        # Print the position and time taken using Binary Search
        elif selection == "2":
            print("\nBinary Search starting...")
            startTime = time.time()
            x = binarySearch(dictionary, word_type)
            endTime = time.time()
            time_elapsed = endTime - startTime
            if x == -1:
                print(word_type + " is NOT IN the dictionary. (" +
                      str(time_elapsed) + " seconds)")
            else:
                print(word_type + " is IN the dictionary at position " +
                      str(x) + ". (" + str(time_elapsed) + " seconds)")
        # Print the number of words and time not found using Linear Search
        elif selection == "3":
            count = 0
            print("\nLinear Search Starting...")
            startTime = time.time()
            for i in range(len(aliceWords)):
                x = linearSearch(dictionary, aliceWords[i].lower())
                if x == -1:
                    count += 1
            endTime = time.time()
            time_elapsed = endTime - startTime
            print("Number of words not found in dictionary: " +
                  str(count) + " (" + str(time_elapsed) + " seconds)")
        # Print the number of words and time not found using Binary Search
        elif selection == "4":
            count = 0
            print("\nBinary Search Starting...")
            startTime = time.time()
            for i in range(len(aliceWords)):
                x = binarySearch(dictionary, aliceWords[i].lower())
                if x == -1:
                    count += 1
            endTime = time.time()
            time_elapsed = endTime - startTime
            print("Number of words not found in dictionary: " +
                  str(count) + " (" + str(time_elapsed) + " seconds)")
        # print goodbye and stop the while loop
        elif selection == "5":
            print("Goodbye!")
            break
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
