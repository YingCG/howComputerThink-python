class UserAccount:

    def __init__(self):
        self.username = "ciars"
        self.password = "1234"
        self.__newpassword = "9876"

    # remove @staticmethod to call this method
    @staticmethod
    def showPassword(self):
        print(f"{self.username} : {self.password}")


user1 = UserAccount()

user1.showPassword()

print(user1.__newpassword)
