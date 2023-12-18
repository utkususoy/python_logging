import logging_config
import logging
from module_2 import module_2_main
from module_1_1 import module_1_1_print

logging_config.setup_logging(log_file="temp_app_logs.log")

# Your module code
logger = logging.getLogger(__name__)

def module_1_main():
    logger.info("Module 1 - Info message")
    module_2_main()
    module_1_1_print(data=3)
    pass

if __name__ == "__main__":
    module_1_main()