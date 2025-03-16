import logging
from con_4_delivery_confirmation.App.consumer import run_consumer

def configure_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"  
    )

if __name__ == "__main__":
    configure_logger()
    run_consumer()