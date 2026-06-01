import logging

def setup_logger():
    logger = logging.getLogger("trading_bot")
    logger.setLevel(logging.DEBUG)

    # File handler
    fh = logging.FileHandler("trading_bot.log")
    fh.setLevel(logging.DEBUG)

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    fh.setFormatter(fmt)
    ch.setFormatter(fmt)

    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger

logger = setup_logger()
