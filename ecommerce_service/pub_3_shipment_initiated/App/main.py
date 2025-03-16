import logging
from pub_3_shipment_initiated.App.publisher import run_publisher

def configure_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"  
    )

if __name__ == "__main__":
    configure_logger()
    run_publisher()