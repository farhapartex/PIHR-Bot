from files import create_and_set_credentials

class Install:
    def __init__(self):
        self.set_up()

    def set_up(self):
        print("One time setup")
        username, password = "", ""
        while True:
            username = input("Enter Your username: ")
            password = input("Enter Your password: ")
            if not username or not password:
                print("Username and password can't be empty, try again!")
            else:
                break
        if create_and_set_credentials(username, password):
            print("Setup is done with credentials")