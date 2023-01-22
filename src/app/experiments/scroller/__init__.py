import logging
import os

_EXPERIMENT_NAME = "scroller"

logger = logging.getLogger(_EXPERIMENT_NAME)

test_var = os.environ.get("PYGAME_TEST_VAR")

logger.info("SCROLLER EXPERIMENT")
logger.info(f"PYGAME_TEST_VAR={test_var}")
