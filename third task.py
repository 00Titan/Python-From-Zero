def main():
    numbers = []
    while True:
        number = int(input("Enter a number: "))

        if number == 0:
            print("Program terminated.")
            break
        numbers.append(number)

    print(f"The size of a list is {len(numbers)}.")

    for i in range(len(numbers)- 1):
        for j in range(i, len(numbers), 1):
            if j == i:
                numbers.remove(numbers[j])

    print(numbers)

main()

#Вариант 2
def main1():
    numbers = []
    while True:
        number = int(input("Enter a number: "))

        if number == 0:
            print("Program terminated.")
            break
        numbers.append(number)

    print(f"The size of a list is {len(numbers)}.")

    numbers = set(numbers)

    print(numbers)

main1()"