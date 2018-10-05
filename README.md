# League Ranking Table Calculator

This is a simple tool to calculate and display a football league ranking table given results.

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

_NOTE:_ The data input file should be text-based in the format of: `[Team1 name] [score], [Team2 name] [score]`

# Tests

To run tests:
1. Activate the virtual environment (if you haven't already): `source venv/bin/activate`
1. Install the testing requirements: `pip install -e ".[testing]"`
1. Run the test suite: `pytest tests/`

# Future work

While this is a light-weight, MVP-esque solution. There are many ways it can be improved, these include:
* Automated continuous integration & development with some tool such as Travis; this will require all tests to pass before code may be merged to master
* Some refactoring i.t.o. a more OO approach if data gets more complicated, e.g. a GameResult object instead of throwing around lists of tuples.
* Main.py starting to look a bit long, some of the logic may be grouped into a separate file & class (such as Presentation).

# Credits

Developed by Boyan Soubachov (boyanvs@gmail.com), 4 October 2018.
