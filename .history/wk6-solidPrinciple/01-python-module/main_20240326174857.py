from person import Person


def main():
    print("Hello, world!")
    name = input("What is your name?")
    person = Person(name)
    person.greet()


if __name__ == "__main__":
    main()
