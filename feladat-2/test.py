from unittest import TestCase
from main import step, special_step, parse_params

class ParameterParsing(TestCase):
    def test__parameter_structure_can_be_parsed(self):
        data = [
            '2\n',
            '1\n',
            '4\n',
            '2\n',
            '1 2\n'
        ]
        expected = [
            [4],
            [1, 2]
        ]
        result = parse_params(data)
        self.assertEquals(expected, result)

    def test__generated_parameters_are_sorted(self):
        data = [
            '1\n',
            '4\n',
            '3 1 4 2\n'
        ]
        expected = [
            [1, 2, 3, 4]
        ]
        result = parse_params(data)
        self.assertEquals(expected, result)


class StepFunctionality(TestCase):
    def test__step_case_1(self):
        data = [0,1,2]
        expected = [0,0,1]
        result = step(data)
        self.assertEquals(expected, result)


class SpecialStepFunctionality(TestCase):
    def test__special_step_divides_biggest_element(self):
        data = [2]
        expected = [1, 1]
        result = special_step(data)
        self.assertEquals(expected, result)

    def test__special_step_result_is_sorted(self):
        data = [3, 4]
        expected = [2, 2, 3]
        result = special_step(data)
        self.assertEquals(expected, result)

    def test__special_step_divides_odd_numbers_too(self):
        data = [3]
        expected = [1, 2]
        result = special_step(data)
        self.assertEquals(expected, result)

