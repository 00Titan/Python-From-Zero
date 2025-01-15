import random

def main():
    file = open("output.txt", "x")
    with open("output.txt", "w") as file:
        for i in range(10):
            number = random.randint(1, 100)
            file.write(f"{number} ")

    total = 0
    with open("output.txt", "r") as file:
        content = file.read()
        print(content)
        numbers = content.split()
        for number in numbers:
            total += int(number)

    print(f"\nThe sum is {total}.")
main()