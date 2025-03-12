from src.models import Package

def test_package_creation():
    package = Package("P001", 10.5, "regular", "Test package")
    assert package.id == "P001"
    assert abs(package.weight - 10.5) < 1e-6
    assert package.category == "regular"
    assert package.description == "Test package"
