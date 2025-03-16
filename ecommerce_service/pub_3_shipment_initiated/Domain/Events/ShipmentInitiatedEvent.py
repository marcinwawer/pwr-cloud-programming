from datetime import date

class ShipmentInitiatedEvent:
    def __init__(self, shipment_id: int, sent_date: date):
        self.shipment_id = shipment_id
        self.sent_date = sent_date

    def __str__(self):
        return (f"{self.shipment_id}|{self.sent_date}")