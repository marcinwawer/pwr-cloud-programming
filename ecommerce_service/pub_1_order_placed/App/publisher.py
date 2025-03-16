import time, logging, random
from pub_1_order_placed.Domain.Events.OrderPlacedEvent import OrderPlacedEvent
from pub_1_order_placed.App.message_broker import MessageBroker

logger = logging.getLogger(__name__)

def run_publisher(interval=5):
    broker = MessageBroker()
    order_id_counter = random.randint(0, 1000)

    try:
        while True:
            event = OrderPlacedEvent(order_id=order_id_counter, customer="John Doe")
            broker.publish_event(event)
            logger.info(f"sent OrderPlacedEvent (order_id={order_id_counter})")
            order_id_counter += 1
            time.sleep(interval)
    except KeyboardInterrupt:
        logger.info("publisher stopped")
    finally:
        broker.close_connection()