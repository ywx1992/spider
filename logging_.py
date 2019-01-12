import logging


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s [%(message)s]',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    )


logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info("this is a info message")
    logger.error("this is a error message")

    logging.debug("this is a debug message")
    logging.warning("this is a warning message")
    logging.warning("this is a warning message")


