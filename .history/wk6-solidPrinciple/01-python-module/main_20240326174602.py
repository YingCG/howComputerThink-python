from person import Person


def main():
    # print("Hello, world!")
    # name = input("What is your name?")
    # person = Person(name)
    # person.greet()

    try:
        person = Person(input("What is your name?"))
        person.greet()
    except:
        print("Hello, world!")


if __name__ == "__main__":
    main()
