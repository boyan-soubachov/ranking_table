import os
import unittest

from ranking_table import main


class MainTestCase(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.test_file_path = 'tmp_test_file.txt'
        self.test_file_data = [f'Team_A {i}, Team_B {i+1}\n' for i in range(4)]
        self.formatted_test_file_data = [
            {'Team_A': 0, 'Team_B': 1},
            {'Team_A': 1, 'Team_B': 2},
            {'Team_A': 2, 'Team_B': 3},
            {'Team_A': 3, 'Team_B': 4},
        ]
        self._create_tmp_file()

    def tearDown(self):
        os.remove(self.test_file_path)
        super().tearDown()

    def _create_tmp_file(self):
        tmp_file = open(self.test_file_path, 'w+')
        tmp_file.writelines(self.test_file_data)
        tmp_file.close()

    def test_get_input_from_file(self):
        res = main._get_input_from_file(self.test_file_path)
        expected_res = self.formatted_test_file_data
        self.assertListEqual(res, expected_res)

    def test_get_input_from_non_existent_file(self):
        res = main._get_input_from_file(self.test_file_path + 'a')
        self.assertIsNone(res)

    def test_convert_raw_input_to_dict_valid_set(self):
        input_data = 'Lions 3, Snakes 8'
        expected_result = {
            'Lions': 3,
            'Snakes': 8
        }
        res = main._convert_raw_input_to_dict(input_data)
        self.assertDictEqual(res, expected_result)

    def test_raw_input_data_formatting_invalid_team_separation(self):
        with self.assertRaises(ValueError):
            main._convert_raw_input_to_dict('Lions 3; Snakes 8')

    def test_raw_input_data_formatting_invalid_team_number(self):
        with self.assertRaises(ValueError):
            main._convert_raw_input_to_dict('Lions 3, Snakes 8, Bob 1')

    def test_raw_input_data_formatting_duplicated_team_name(self):
        with self.assertRaises(ValueError):
            main._convert_raw_input_to_dict('Lions 3, Lions 8')

    def test_raw_input_data_formatting_case_insensitivity(self):
        with self.assertRaises(ValueError):
            main._convert_raw_input_to_dict('lions 3, Lions 8')

    def test_raw_input_data_formatting_invalid_score_separation(self):
        with self.assertRaises(ValueError):
            main._get_individual_score('Snakes8')

    def test_raw_input_data_formatting_invalid_score_float(self):
        with self.assertRaises(ValueError):
            main._get_individual_score('Snakes 8.4')

    def test_raw_input_data_formatting_invalid_score_non_numeric(self):
        with self.assertRaises(ValueError):
            main._get_individual_score('Snakes abc')
