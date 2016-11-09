from unittest import TestCase
from p3 import parse_params, decision

class ParameterParsing(TestCase):
    def test__parameters_can_be_parsed(self):
        data = [
            '1\n',
            '3 3 1\n'
        ]
        expected = {
            1: [3, 3, 1]
        }
        result = parse_params(data)
        self.assertEquals(expected, result)

    def test__multiple_cases(self):
        data = [
            '3\n',
            '3 3 1\n',
            '4 3 2\n',
            '3 1 1\n'
        ]
        expected = {
            1: [3, 3, 1],
            2: [4, 3, 2],
            3: [3, 1, 1]
        }
        result = parse_params(data)
        self.assertEquals(expected, result)


class BasicFunctionality(TestCase):
    def test__simplest_case(self):
        """
        *
        """
        n = 1
        m = 1
        x = 1
        expected = False
        result = decision(n, m, x)
        self.assertEquals(expected, result)

    def test__1x2_1(self):
        """
        1*
        """
        n = 1
        m = 2
        x = 1
        expected = False
        result = decision(n, m, x)
        self.assertEquals(expected, result)

    def test__1x3_1(self):
        """
        01*
        """
        n = 1
        m = 3
        x = 1
        expected = True
        result = decision(n, m, x)
        self.assertEquals(expected, result)

    def test__1x3_3(self):
        """
        1**
        """
        n = 1
        m = 3
        x = 2
        expected = False
        result = decision(n, m, x)
        self.assertEquals(expected, result)

    def test__case_2x2_1(self):
        """
        11
        1*
        """
        n = 2
        m = 2
        x = 1
        expected = False
        result = decision(n, m, x)
        self.assertEquals(expected, result)

    def test__case_2x2_2(self):
        """
        2*
        2*
        """
        n = 2
        m = 2
        x = 2
        expected = False
        result = decision(n, m, x)
        self.assertEquals(expected, result)

    def test__case_3x3_1(self):
        """
        000
        011
        01*
        """
        n = 3
        m = 3
        x = 1
        expected = True
        result = decision(n, m, x)
        self.assertEquals(expected, result)

    def test__case_3x3_2(self):
        """
        000
        122
        1**
        """
        n = 3
        m = 3
        x = 2
        expected = False
        result = decision(n, m, x)
        self.assertEquals(expected, result)

    def test__case_3x3_3(self):
        """
        000
        232
        ***
        """
        n = 3
        m = 3
        x = 3
        expected = True
        result = decision(n, m, x)
        self.assertEquals(expected, result)

    def test__case_3x3_4(self):
        """
        011
        24*
        ***
        """
        n = 3
        m = 3
        x = 4
        expected = False
        result = decision(n, m, x)
        self.assertEquals(expected, result)


    def test__case_3x3_5(self):
        """
        02*
        23*
        ***
        """
        n = 3
        m = 3
        x = 5
        expected = True
        result = decision(n, m, x)
        self.assertEquals(expected, result)

    def test__case_3x3_6(self):
        """
        13*
        3**
        ***
        """
        n = 3
        m = 3
        x = 6
        expected = False
        result = decision(n, m, x)
        self.assertEquals(expected, result)

    def test__case_3x4_8(self):
        """
        02**
        25**
        ****
        """
        n = 3
        m = 4
        x = 8
        expected = True
        result = decision(n, m, x)
        self.assertEquals(expected, result)

    def test__case_3x4_9(self):
        """
        13**
        3***
        ****
        """
        n = 3
        m = 4
        x = 9
        expected = False
        result = decision(n, m, x)
        self.assertEquals(expected, result)

    def test__case_3x4_5(self):
        """
        0011
        233*
        ****
        """
        n = 3
        m = 4
        x = 5
        expected = False
        result = decision(n, m, x)
        self.assertEquals(expected, result)

    def test__case_4x7_24(self):
        """
        02*****
        25*****
        *******
        *******
        """
        n = 4
        m = 7
        x = 24
        expected = True
        result = decision(n, m, x)
        self.assertEquals(expected, result)

    def test__case_5x5_15(self):
        """
        00000
        23332
        *****
        *****
        *****
        """
        n = 5
        m = 5
        x = 15
        expected = True
        result = decision(n, m, x)
        self.assertEquals(expected, result)

    def test__case_5x5_14(self):
        """
        00000
        12332
        3****
        *****
        *****
        """
        n = 5
        m = 5
        x = 14
        expected = False
        result = decision(n, m, x)
        self.assertEquals(expected, result)

    def test__case_5x5_13(self):
        """
        00000
        01232
        24***
        *****
        *****
        """
        n = 5
        m = 5
        x = 13
        expected = True
        result = decision(n, m, x)
        self.assertEquals(expected, result)

    def test__case_5x5_4(self):
        """
        00000
        00000
        00011
        0124*
        01***
        """
        n = 5
        m = 5
        x = 4
        expected = True
        result = decision(n, m, x)
        self.assertEquals(expected, result)
