import time, logging
from datetime import datetime, timedelta
from con_3_shipment_notification.Domain.Events.ShipmentInitiatedEvent import ShipmentInitiatedEvent
from con_3_shipment_notification.Domain.Events.ShipmentDeliveredEvent import ShipmentDeliveredEvent
from con_3_shipment_notification.App.message_broker import MessageBroker

logger = logging.getLogger(__name__)

def process_shipment(message_str: str):
    parts = message_str.split("|")
    if len(parts) == 2:
        shipment_id, sent_date = parts
        logger.info(f"processing shipment: shipment_date={shipment_id}, sent_date={sent_date}")
        time.sleep(2)
        return shipment_id, sent_date
    else:
        logger.warning("incorrect message format")
        return None, None

def run_consumer():
    broker = MessageBroker()

    def callback(msg_str: str):
        shipment_id, sent_date = process_shipment(msg_str)

        if shipment_id is None or sent_date is None:
            return
        
        sent_date_obj = datetime.strptime(sent_date, "%Y-%m-%d").date()
        delivery_date = sent_date_obj + timedelta(days=5)
        new_event = ShipmentDeliveredEvent(shipment_id=shipment_id, delivery_date=delivery_date)

        broker.publish_event(new_event)
        logger.info(f"published ShipmentDeliveredEvent for shipment_id={shipment_id}")
        
    broker.consume_event(ShipmentInitiatedEvent, callback)