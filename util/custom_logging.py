import logging


logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] - %(levelname)s - %(message)s',
    datefmt="%d/%b/%Y %H:%M:%S"
)

DEBUG_COLOR = "\x1b[33m"
INFO_COLOR = "\x1b[36m"
CRITICAL_COLOR = "\x1b[1;31m"
RESET_COLOR = "\x1b[0m"
WARNING_COLOR = "\x1b[1;33m"


def debug(message: str):
    return logging.debug(f"{DEBUG_COLOR}{message}{RESET_COLOR}")


def warning(message: str):
    return logging.warning(f"{WARNING_COLOR}{message}{RESET_COLOR}")


def critical(message: str):
    return logging.critical(f"{CRITICAL_COLOR}{message}{RESET_COLOR}")


def info(message: str):
    return logging.info(f"{INFO_COLOR}{message}{RESET_COLOR}")
