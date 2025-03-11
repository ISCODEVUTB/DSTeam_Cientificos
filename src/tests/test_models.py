from src.models import Package, Shipment, User

def test_package_creation():
    package = Package("P001", 10.5, "regular", "Test package")
    assert package.id == "P001"
    assert package.weight == 10.5
    assert package.category == "regular"
    assert package.description == "Test package"

def test_shipment_creation():
    shipment = Shipment("S001", "John Doe")
    assert shipment.id == "S001"
    assert shipment.recipient == "John Doe"
    assert len(shipment.packages) == 0
    assert shipment.status == "In transit"

def test_user_authentication():
    user = User("testuser", "password123")
    assert user.authenticate("password123") == True
    assert user.authenticate("wrongpassword") == False 