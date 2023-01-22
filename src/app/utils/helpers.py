import logging

LOG_FORMAT = "%(levelname)5s: %(message)s"


def setup_logger(debug=False):
    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO, format=LOG_FORMAT
    )
