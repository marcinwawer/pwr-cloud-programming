from datetime import date

class ShipmentDeliveredEvent:
    def __init__(self, shipment_id: int, delivery_date: date):
        self.shipment_id = shipment_id
        self.delivery_date = delivery_date

    def __str__(self):
        return f"{self.shipment_id}|{self.delivery_date}"