from unittest import TestCase
from f1 import parse_params

class ParameterParsing(TestCase):
    def test__parameter_parsing_case_1(self):
        data = [
            '2\n',
            '1\n',
            '4\n',
        ]
        expected = [1, 4]
        result = parse_params(data)
        self.assertEquals(expected, result)

