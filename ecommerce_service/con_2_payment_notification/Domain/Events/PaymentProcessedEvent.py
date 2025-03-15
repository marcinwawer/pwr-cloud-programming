class PaymentProcessedEvent:
    def __init__(self, payment_id: int, amount: float):
        self.payment_id = payment_id
        self.amount = amount

    def __str__(self):
        return (f"{self.payment_id}|{self.amount}")