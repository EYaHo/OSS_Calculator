import logging

def getLogger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s")

    file_Handler_Info = logging.FileHandler(filename = "info.log")
    file_Handler_Warning = logging.FileHandler(filename = "warning.log")

    file_Handler_Info.setLevel(logging.INFO)
    file_Handler_Warning.setLevel(logging.WARNING)

    file_Handler_Info.setFormatter(formatter)
    file_Handler_Warning.setFormatter(formatter)

    logger.addHandler(file_Handler_Info)
    logger.addHandler(file_Handler_Warning)

    return logger