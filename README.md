# PyGame Experiments

Home to various experiments, half-baked ideas, useful snippets and other PyGame related resources.

## Installation

Create and activate a Python `virtualenv` and then install required dependencies:

    python3 -m venv ./venv
    source ./venv/bin/activate
    pip install -r ./requirements.txt

## Configuration

Configuration for all experiments are managed by `dotenv`. Copy the provided [`.env.example`](./.env.example) to `.env` and add or modify any required configuration values. These values will automatically sourced and can be accessed as environment variables (i.e. `os.environ.get("SDL_VIDEODRIVER")`).

## Usage

Run existing experiment (e.g. `scroller`):

    (cd ./src && python3 -m app -e scroller)
