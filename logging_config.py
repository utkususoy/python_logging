import logging

def setup_logging(log_file="default_log.log"):
    # # Configure logging
    logging.basicConfig(level=logging.DEBUG)

    # Create a file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(funcName)s - %(exc_info)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    file_handler.setFormatter(formatter)


    root_logger = logging.getLogger()
    root_logger.addHandler(file_handler)
