from typing import Dict, List
from functools import cmp_to_key


class LeagueTable(object):
    def __init__(self):
        self.points_table = {}

    def add_result(self, score_set: Dict):
        team_points = self._get_points(score_set)

        for team, points in team_points.items():
            if team in self.points_table:
                self.points_table[team] += points
            else:
                self.points_table[team] = points

    def _get_points(self, score_set: Dict) -> Dict:
        scores_tuples = sorted(
            score_set.items(),
            key=lambda item: item[1],
            reverse=True
        )

        first_team_name = scores_tuples[0][0]
        first_team_score = scores_tuples[0][1]

        second_team_name = scores_tuples[1][0]
        second_team_score = scores_tuples[1][1]

        # 2 possible combinations, a team wins while another loses or they both draw
        # the sort above ensures the first team listed is the one with the highest score
        if first_team_score > second_team_score:
            return {
                first_team_name: 3,
                second_team_name: 0
            }
        else:
            return {
                first_team_name: 1,
                second_team_name: 1
            }

    def get_current_standings(self) -> List[Dict]:  # Can do an OrderedDict here but overkill
        sorted_points_table = sorted(
            self.points_table.items(),
            key=lambda row: (-row[1], row[0])
        )
        res = [{row[0]:row[1]} for row in sorted_points_table]
        return res
