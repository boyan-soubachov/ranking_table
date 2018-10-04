from typing import Dict, List, Tuple

import click

from ranking_table.league_table import LeagueTable


@click.command()
@click.option('--file', help='An absolute path to a text file containing match results')
def main(file):
    input_data = None

    if file:
        input_data = _get_input_from_file(file)
    else:
        input_data = _get_input_from_stdin()

    if not input_data:
        print('-Empty league table-')
        return

    league_table = LeagueTable()
    for row in input_data:
        league_table.add_result(row)

    result_table = league_table.get_current_standings()
    formatted_results = _get_formatted_league_table_results(result_table)
    for line in formatted_results:
        print(line)


def _get_input_from_file(path: str) -> List[Dict]:
    try:
        file_data = open(path, 'r')
    except FileNotFoundError:
        print('The file at the specified path doesn\'t exist')
        return None

    res = []
    for line in file_data:
        scores = _convert_raw_input_to_dict(line)
        res.append(scores)

    return res


def _get_input_from_stdin() -> List[Dict]:
    print('Please enter your data in the format, specified by the README.md file, below.')
    print('When entering your input, press enter to input a new result. Input an empty set to signify the end of data.')

    inp_data = []
    user_input = input('Scores: ')
    while (user_input != ''):
        scores = _convert_raw_input_to_dict(user_input)
        inp_data.append(scores)
        user_input = input('Scores: ')

    return inp_data


def _convert_raw_input_to_dict(raw_input: str) -> Dict:
    # Could go with regex for this but it may be overkill, keeping it MVP for now.
    res = {}
    pairs = raw_input.split(',')

    if not len(pairs) == 2:
        raise ValueError(f'Input data format invalid: {raw_input}')

    for pair in pairs:
        try:
            team_name, team_score = _get_individual_score(pair)
        except ValueError as error:
            raise ValueError(f'Input data error: {str(error)} for input line {raw_input}')

        if team_name in res:
            raise ValueError(f'Ambiguous score; team name repeated: {raw_input}')

        res[team_name] = team_score

    return res


def _get_individual_score(string_input: str) -> Tuple[str, int]:
    data = string_input.strip().split(' ')
    if not len(data) == 2:
        raise ValueError(f'Individual score format invalid')

    team_name = data[0].title()

    if not data[1].isdigit():
        raise ValueError(f'Only valid, integer scores allowed')
    team_score = int(data[1])

    return team_name, team_score


def _get_formatted_league_table_results(league_table: LeagueTable) -> List[str]:
    output_lines = []
    last_position = -1
    last_points = -1

    for row_number, row in enumerate(league_table.get_current_standings()):
        team_name = row[0]
        team_points = row[1]

        if team_points != last_points:
            last_position = row_number + 1

        text = '{pos}. {team_name}, {points} {plural}'.format(
            pos=last_position if team_points == last_points else row_number + 1,
            team_name=team_name,
            points=team_points,
            plural='pt' if team_points == 1 else 'pts'
        )
        last_points = team_points
        output_lines.append(text)
    return output_lines
