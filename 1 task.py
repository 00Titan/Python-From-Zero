def main():
    print("What is your name?")
    name = input()

    print("How old are you?")
    age = input()
    age1 = int(age) + 5
    print("Hello, "+name+"! In 5 years you will be "+ str(age1) + " years old.")

main()