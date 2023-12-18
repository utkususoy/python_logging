import logging

def module_1_1_print(data):
    try:
        logging.info("Module 1.1 - Info message")
        print("This is module 1.1")
        data = "5" + data
        print(data)
    except Exception as e:
        logging.exception(e)