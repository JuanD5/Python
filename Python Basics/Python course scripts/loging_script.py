import logging
logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    level=logging.INFO,
                    filename='logs.txt')
# logging.basicConfig(format='%(asctime)s %(levelname)-8s: %(message)s',
#                   level=logging.INFO)
logger = logging.getLogger("test_logger")
logger.info("Hello")
logger.warning("Stoppp")
