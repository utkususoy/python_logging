import logging_config
import logging
from module_1_1 import module_1_1_print

def module_2_main():
    logging.info("Module 2 - Info message")
    module_1_1_print(data="5")
    pass

if __name__ == "__main__":
    module_2_main()