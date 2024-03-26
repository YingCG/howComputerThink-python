from person import Person


def main():
    # Creating a Person object with password
    person_with_password = Person("Alice", "password123")
    person_with_password.greet()
    person_with_password.login()

    # Creating a Person object without password
    person_without_password = Person("Bob")
    person_without_password.greet()
    person_without_password.login()


if __name__ == "__main__":
    main()
