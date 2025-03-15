import time, logging
from con_1_order_notification.Domain.Events.OrderPlacedEvent import OrderPlacedEvent
from con_1_order_notification.App.message_broker import MessageBroker

logger = logging.getLogger(__name__)

def process_order_placed(message_str: str):
    parts = message_str.split("|")
    if len(parts) == 2:
        order_id, customer = parts
        logger.info(f"processing order: order_id={order_id}, customer={customer}")
        time.sleep(2)
    else:
        logger.warning("incorrect message format")

def run_consumer():
    broker = MessageBroker()

    def callback(msg_str: str):
        process_order_placed(msg_str)

    broker.consume_event(OrderPlacedEvent, callback)