from datetime import date

class ShipmentDeliveredEvent:
    def __init__(self, shipment_id: int, delivered_date: date):
        self.shipment_id = shipment_id
        self.delivered_date = delivered_date

    def __str__(self):
        return f"{self.shipment_id}|{self.delivered_date}"