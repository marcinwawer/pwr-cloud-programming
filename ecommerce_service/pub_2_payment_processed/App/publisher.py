import time, logging, random
from pub_2_payment_processed.Domain.Events.PaymentProcessedEvent import PaymentProcessedEvent
from pub_2_payment_processed.App.message_broker import MessageBroker

logger = logging.getLogger(__name__)

def run_publisher():
    broker = MessageBroker()
    payment_id_counter = random.randint(0, 1000)

    try:
        while True:
            event = PaymentProcessedEvent(payment_id=payment_id_counter, amount=7.40)
            broker.publish_event(event)
            logger.info(f"sent PaymentProcessedEvent (payment_id={payment_id_counter})")
            payment_id_counter += 1
            time.sleep(random.uniform(1, 10))
    except KeyboardInterrupt:
        logger.info("publisher stopped")
    finally:
        broker.close_connection()