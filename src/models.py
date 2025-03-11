class Package:
    """
    Class to represent a package.
    """

    def __init__(self, id, weight, category, description):
        """
        Initialize a new package.

        Args:
            id: Package ID
            weight: Package weight in kg
            category: Package category (elemental, regular, volumetric)
            description: Package description
        """
        self.id = id
        self.weight = weight
        self.category = category
        self.description = description

    def show_info(self):
        """
        Display package information.
        """
        print(
            f"Package ID: {self.id}, Weight: {self.weight} kg, "
            f"Category: {self.category}, Description: {self.description}"
        )


class Shipment:
    """
    Class to represent a shipment.
    """

    def __init__(self, id, recipient):
        """
        Initialize a new shipment.

        Args:
            id: Shipment ID
            recipient: Recipient name
        """
        self.id = id
        self.recipient = recipient
        self.packages = []
        self.status = "In transit"

    def add_package(self, package):
        """
        Add a package to the shipment.

        Args:
            package: Package object to add
        """
        self.packages.append(package)

    def show_info(self):
        """
        Display shipment information.
        """
        print(
            f"Shipment ID: {self.id}, "
            f"Recipient: {self.recipient}, "
            f"Status: {self.status}"
        )
        print("Packages in this shipment:")
        for package in self.packages:
            package.show_info()

    def update_status(self, new_status):
        """
        Update the status of the shipment.

        :param new_status: New status of the shipment
        """
        self.status = new_status
        print(f"Shipment {self.id} status updated to: {self.status}")


class User:
    """
    Class to represent a user.
    """

    def __init__(self, username, password):
        """
        Initialize a new user.

        :param username: Username
        :param password: Password
        """
        self.username = username
        self.password = password

    def authenticate(self, input_password):
        """
        Authenticate the user.

        :param input_password: Password to authenticate
        :return: True if authentication is successful, False otherwise
        """
        return self.password == input_password
