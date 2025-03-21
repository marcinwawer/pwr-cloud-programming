import pika, logging, sys

logger = logging.getLogger(__name__)

class MessageBroker:
    def __init__(self, host="localhost"):
        try:
            self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=host)
            )

            self.channel = self.connection.channel()
            logger.info("connected to rabbitmq (publisher 2)")
        except Exception as e:
            logger.error(f"connection error: {e}")
            sys.exit(1)

    def publish_event(self, event):
        queue_name = type(event).__name__
        self.channel.queue_declare(queue=queue_name)

        body = str(event)

        self.channel.basic_publish(
            exchange='',
            routing_key=queue_name,
            body=body.encode('utf-8')
        )

        logger.info(
            f"event published: {queue_name}, "
            f"payment_id={event.payment_id}, amount={event.amount}"
        )

    def close_connection(self):
        self.connection.close()
        logger.info("closed connection (publisher 2)")