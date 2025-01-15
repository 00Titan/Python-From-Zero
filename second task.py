def main():
    number = 1

    while number != 0:
        number = int(input("Enter a number: "))
        if number == 0:
            break

        if number % 2 == 0:
            print("It is even number!\n")
        else:
            print("It is not even number!\n")

main()