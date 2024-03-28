from person import Person


def main():
    # Creating a Person object with password
    somebody = Person(input("what is your name?"))
    somebody.greet()
    # somebody.addproduct()
    somebody.login()
    public = Person(
        "admin",
    )
    # public.addToShopping()
    # # Creating a Person object without password
    # person_without_password = Person(input("what is your name?"))
    # person_without_password.greet()
    # person_without_password.login()


if __name__ == "__main__":
    main()
