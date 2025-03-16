import logging
from con_3_shipment_notification.App.consumer import run_consumer

def configure_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"  
    )

if __name__ == "__main__":
    configure_logger()
    run_consumer()