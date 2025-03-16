import time, logging
from con_4_delivery_confirmation.Domain.Events.ShipmentDeliveredEvent import ShipmentDeliveredEvent
from con_4_delivery_confirmation.App.message_broker import MessageBroker

logger = logging.getLogger(__name__)

def process_delivery(message_str: str):
    parts = message_str.split("|")
    if len(parts) == 2:
        shipment_id, delivery_date = parts
        logger.info(f"processing delivery: shipment_id={shipment_id}, delivery_date={delivery_date}")
        time.sleep(2)
    else:
        logger.warning("incorrect message format")

def run_consumer():
    broker = MessageBroker()

    def callback(msg_str: str):
        process_delivery(msg_str)

    broker.consume_event(ShipmentDeliveredEvent, callback)