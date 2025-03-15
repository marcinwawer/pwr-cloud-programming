class OrderPlacedEvent:
    def __init__(self, order_id: int, customer: str):
        self.order_id = order_id
        self.customer = customer
    
    def __str__(self):
        return f"{self.order_id}|{self.customer}"