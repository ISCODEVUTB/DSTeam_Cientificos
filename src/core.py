from src.models import User
from src.utils import (
    register_package,
    create_shipment,
    add_package_to_shipment,
    show_shipments
)


class LogisticsSystem:
    """
    Main class for the logistics system.
    """

    def __init__(self):
        """
        Initialize the logistics system.
        """
        self.packages = []
        self.shipments = []
        self.users = {}

    def register_user(self):
        """
        Register a new user.
        """
        username = input("Enter username: ")
        password = input("Enter password: ")

        self.users[username] = User(username, password)
        print("User registered successfully.")

    def authenticate_user(self):
        """
        Authenticate a user.

        :return: True if authentication is successful, False otherwise
        """
        username = input("Enter username: ")
        password = input("Enter password: ")

        user = self.users.get(username)
        if user and user.authenticate(password):
            print("Authentication successful.")
            return True
        print("Authentication failed.")
        return False

    def register_package(self):
        """
        Register a new package.
        """
        register_package(self.packages)

    def create_shipment(self):
        """
        Create a new shipment.
        """
        create_shipment(self.shipments)

    def add_package_to_shipment(self):
        """
        Add a package to an existing shipment.
        """
        add_package_to_shipment(self.packages, self.shipments)

    def show_shipments(self):
        """
        Display information of all shipments.
        """
        show_shipments(self.shipments)


def show_menu():
    """
    Display the main menu.
    """
    print("\n--- Logistics System Menu ---")
    print("1. Register user")
    print("2. Authenticate user")
    print("3. Register package")
    print("4. Create shipment")
    print("5. Add package to shipment")
    print("6. Show shipments")
    print("7. Exit")
    return int(input("Select an option: "))


def main():
    """
    Main function to run the logistics system.
    """
    system = LogisticsSystem()
    while True:
        option = show_menu()
        if option == 1:
            system.register_user()
        elif option == 2:
            if system.authenticate_user():
                print("User authenticated successfully.")
            else:
                print("Authentication failed.")
        elif option == 3:
            system.register_package()
        elif option == 4:
            system.create_shipment()
        elif option == 5:
            system.add_package_to_shipment()
        elif option == 6:
            system.show_shipments()
        elif option == 7:
            print("Exiting the system...")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
