def main():
    dictionary = {}
    print("Enter sentense (empty line to finish):")

    while True:
        sentense = input()

        if sentense == "":
            print("Program terminated.")
            break

        words = sentense.split()
        for word in words:
            word = word.lower()
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1

    print("Word counts:")
    print(dictionary)

main()