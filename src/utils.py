from src.models import Package, Shipment


def register_package(packages):
    """
    Register a new package.

    :param packages: List of packages
    """
    package_id = input("Enter package ID: ")
    weight = float(input("Enter package weight (kg): "))
    category = input("Enter category (elemental, regular, volumetric): ")
    description = input("Enter package description: ")

    new_package = Package(package_id, weight, category, description)
    packages.append(new_package)
    print("Package registered successfully.")


def create_shipment(shipments):
    """
    Create a new shipment.

    :param shipments: List of shipments
    """
    shipment_id = input("Enter shipment ID: ")
    recipient = input("Enter recipient name: ")

    new_shipment = Shipment(shipment_id, recipient)
    shipments.append(new_shipment)
    print("Shipment created successfully.")


def add_package_to_shipment(packages, shipments):
    """
    Add a package to an existing shipment.

    Args:
        packages: List of packages
        shipments: List of shipments
    """
    shipment_id = input("Enter shipment ID: ")
    package_id = input("Enter package ID: ")

    found_package = next(
        (pkg for pkg in packages if pkg.id == package_id),
        None
    )

    if found_package:
        found_shipment = next(
            (shp for shp in shipments if shp.id == shipment_id),
            None
        )
        if found_shipment:
            found_shipment.add_package(found_package)
            print(f"Package added to shipment {shipment_id}")
        else:
            print("Shipment not found.")
    else:
        print("Package not found.")


def show_shipments(shipments):
    """
    Display information of all shipments.

    :param shipments: List of shipments
    """
    if not shipments:
        print("No shipments registered.")
    else:
        for shipment in shipments:
            shipment.show_info()
