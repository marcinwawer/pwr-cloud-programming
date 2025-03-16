import time, logging, random
from datetime import date, timedelta
from pub_3_shipment_initiated.Domain.Events.ShipmentInitiatedEvent import ShipmentInitiatedEvent
from pub_3_shipment_initiated.App.message_broker import MessageBroker

logger = logging.getLogger(__name__)

def random_date(start: date, end: date) -> date:
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

def run_publisher():
    broker = MessageBroker()
    shipment_id_counter = random.randint(0, 1000)
    start_date = date(2025, 1, 1)
    end_date = date(2025, 12, 31)

    try:
        while True:
            sent_date = random_date(start_date, end_date)
            event = ShipmentInitiatedEvent(shipment_id=shipment_id_counter, sent_date=sent_date)
            broker.publish_event(event)
            logger.info(f"sent ShipmentInitiatedEvent (shipment_id={shipment_id_counter})")
            shipment_id_counter += 1
            time.sleep(random.uniform(1, 10))
    except KeyboardInterrupt:
        logger.info("publisher stopped")
    finally:
        broker.close_connection()