from .files import create_and_set_credentials

class Install:
    def __init__(self):
        self._set_up()

    def _set_up(self):
        print("One time setup")
        username, password = "", ""
        while True:
            username = input("Enter Your username: ")
            password = input("Enter Your password: ")
            company = input("Enter Your company: ")
            if not username or not password or not company:
                print("Username, password and company can't be empty, try again!")
            else:
                break
        if create_and_set_credentials(username, password, company):
            print("Setup is done with credentials")
            print("Make sure your RabbitMQ server is running before running below command")
            print("Run python3 init.py run")