import unittest
from ranking_table import league_table


class LeageTableTestCase(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.table = league_table.LeagueTable()

    def test_get_points_win_team_a(self):
        expected_result = {'Team_A': 3, 'Team_B': 0}
        res = self.table._get_points({'Team_A': 1, 'Team_B': 0})

        self.assertDictEqual(res, expected_result)

    def test_get_points_win_team_b(self):
        expected_result = {'Team_A': 0, 'Team_B': 3}
        res = self.table._get_points({'Team_A': 1, 'Team_B': 8})

        self.assertDictEqual(res, expected_result)

    def test_get_points_draw(self):
        expected_result = {'Team_A': 1, 'Team_B': 1}
        res = self.table._get_points({'Team_A': 0, 'Team_B': 0})

        self.assertDictEqual(res, expected_result)

    def test_add_result(self):
        expected_result = {'Team_A': 3, 'Team_B': 0}
        self.table.add_result({'Team_A': 8, 'Team_B': 4})

        self.assertDictEqual(self.table.points_table, expected_result)

    def test_get_sorted_points_table_win_loss(self):
        expected_result = [
            ('Team_B', 3),
            ('Team_A', 0)
        ]
        self.table.add_result({'Team_A': 0, 'Team_B': 4})
        res = self.table.get_current_standings()
        self.assertListEqual(res, expected_result)

    def test_get_sorted_points_table_draw(self):
        expected_result = [
            ('Team_A', 1),
            ('Team_B', 1)
        ]
        self.table.add_result({'Team_A': 0, 'Team_B': 0})
        res = self.table.get_current_standings()
        self.assertListEqual(res, expected_result)

    def test_get_sorted_points_team_name_sorting(self):
        expected_result = [
            ('Team_A', 1),
            ('Team_B', 1),
            ('Team_C', 1),
            ('Team_D', 1),
        ]
        input_data = {
            'Team_D': 1,
            'Team_B': 1,
            'Team_C': 1,
            'Team_A': 1
        }

        res = self.table._get_sorted_points_table(input_data)
        self.assertListEqual(res, expected_result)

    def test_get_sorted_points_table_example(self):
        expected_result = [
            ('Tarantulas', 6),
            ('Lions', 5),
            ('FC Awesome', 1),
            ('Snakes', 1),
            ('Grouches', 0),
        ]
        self.table.add_result({'Lions': 3, 'Snakes': 3})
        self.table.add_result({'Tarantulas': 1, 'FC Awesome': 0})
        self.table.add_result({'Lions': 1, 'FC Awesome': 1})
        self.table.add_result({'Tarantulas': 3, 'Snakes': 1})
        self.table.add_result({'Lions': 4, 'Grouches': 0})

        res = self.table.get_current_standings()
        self.assertListEqual(res, expected_result)
