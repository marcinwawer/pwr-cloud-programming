import time, logging
from con_3_shipment_notification.Domain.Events.ShipmentInitiatedEvent import ShipmentInitiatedEvent
from con_3_shipment_notification.App.message_broker import MessageBroker

logger = logging.getLogger(__name__)

def process_order_placed(message_str: str):
    parts = message_str.split("|")
    if len(parts) == 2:
        shipment_id, sent_date = parts
        logger.info(f"processing payment: shipment_date={shipment_id}, sent_date={sent_date}")
        time.sleep(2)
    else:
        logger.warning("incorrect message format")

def run_consumer():
    broker = MessageBroker()

    def callback(msg_str: str):
        process_order_placed(msg_str)

    broker.consume_event(ShipmentInitiatedEvent, callback)