import time, logging
from con_2_payment_notification.Domain.Events.PaymentProcessedEvent import PaymentProcessedEvent
from con_2_payment_notification.App.message_broker import MessageBroker

logger = logging.getLogger(__name__)

def process_payment(message_str: str):
    parts = message_str.split("|")
    if len(parts) == 2:
        payment_id, amount = parts
        logger.info(f"processing payment: payment_id={payment_id}, amount={amount}")
        time.sleep(2)
    else:
        logger.warning("incorrect message format")

def run_consumer():
    broker = MessageBroker()

    def callback(msg_str: str):
        process_payment(msg_str)

    broker.consume_event(PaymentProcessedEvent, callback)