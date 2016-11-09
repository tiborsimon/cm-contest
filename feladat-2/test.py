from unittest import TestCase
from f2 import step, special_step, parse_params, calculate_steps, finish


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


class FinishDecision(TestCase):
    def test__all_zero_plate_set__returns_true(self):
        data = [
            [0, 0]
        ]
        expected = True
        result = finish(data)
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


class StepCalculation(TestCase):
    def test__special_step_divides_biggest_element(self):
        data = [2]
        expected = 2
        result = calculate_steps(data)
        self.assertEquals(expected, result)

    def test__consider_special_steps(self):
        data = [4]
        expected = 3
        result = calculate_steps(data)
        self.assertEquals(expected, result)
