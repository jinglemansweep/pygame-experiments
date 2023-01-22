import logging
from argparse import ArgumentParser
from dotenv import load_dotenv, find_dotenv
from app.utils.helpers import setup_logger

_APP_NAME = "pygame-experiments"
_APP_DESCRIPTION = "PyGame Experiments"
_APP_VERSION = "0.0.1"

load_dotenv(find_dotenv())

EXPERIMENTS = ["scroller"]

parser = ArgumentParser(
    prog=f"{_APP_NAME} v{_APP_VERSION}",
    description=f"{_APP_DESCRIPTION}",
)
parser.add_argument("-e", "--experiment", choices=EXPERIMENTS, required=True)
parser.add_argument("-v", "--verbose", action="store_true")

args = parser.parse_args()
setup_logger(debug=args.verbose)
logger = logging.getLogger("main")

logger.info("PyGame Experiments")
logger.info(f"Experiment: {args.experiment}")
logger.debug("debug message")

match args.experiment:
    case "scroller":
        from app.experiments import scroller
