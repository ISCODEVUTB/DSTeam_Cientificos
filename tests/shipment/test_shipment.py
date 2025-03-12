from src.models import Shipment

def test_shipment_creation():
    shipment = Shipment("S001", "John Doe")
    assert shipment.id == "S001"
    assert shipment.recipient == "John Doe"
    assert len(shipment.packages) == 0
    assert shipment.status == "In transit"
