import pika, logging, sys

logger = logging.getLogger(__name__)

class MessageBroker:
    def __init__(self, host="localhost"):
        try:
            self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=host)
            )

            self.channel = self.connection.channel()
            logger.info("connected to rabbitmq (consumer 3)")
        except Exception as e:
            logger.error(f"conection error: {e}")
            sys.exit(1)

    def consume_event(self, event_class, callback):
        queue_name = event_class.__name__
        self.channel.queue_declare(queue=queue_name)
        logger.info(f"queue subscription: {queue_name}")

        def on_message(ch, method, properties, body):
            msg_str = body.decode('utf-8')
            logger.info(f"message received: {msg_str} in queue {queue_name}")
            callback(msg_str)
            ch.basic_ack(delivery_tag=method.delivery_tag)

        self.channel.basic_consume(queue=queue_name, on_message_callback=on_message)
        logger.info("starting listening... (ctrl+c to interrupt)")
        
        try:
            self.channel.start_consuming()
        except KeyboardInterrupt:
            logger.info("consumer stopped")
            self.channel.stop_consuming()
        finally:
            self.close_connection()

    def close_connection(self):
        self.connection.close()
        logger.info("connection closed (consumer 2).")