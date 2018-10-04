# About

This is a simple tool to calculate and display a football ranking table given results.

# Requirements

* Python 3 or later
* Pip (for dependency installation)

It is also recommended to have a virtual environment manager such as `virtualenv` or `pipenv`.
Instructions in this readme file will assume `virtualenv`.

# Installation

1. Create and activate a Python 3 virtual environment: ```virtualenv venv && source venv/bin/activate```
1. Install the `ranking_table` package: ```pip install -e .```

✨ 🍰, you're done!


# Usage

Input is taken in two ways, either line-by-line through console stdin or piped in through a file (using the `--file` option).

## Stdin

Just run the program by entering `ranking_table` with no options in console. Follow the prompted instructions.

## File

Simply specify the `--file {path_to_data_file}` option with an absolute path to your input data file.

_NOTE:_ The data input file should be text-based in the format of: `[Team1 name, no spaces] [score], [Team2 name, no spaces] [score]`

# Tests

To run tests:
1. Activate the virtual environment (if you haven't already): `source venv/bin/activate`
1. Install the testing requirements: `pip install -e ".[testing]"`
1. Run the test suite: `pytest tests/`

# Credits

Developed and copyright by Boyan Soubachov (boyanvs@gmail.com), 4 October 2018.
