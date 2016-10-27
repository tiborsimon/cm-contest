from unittest import TestCase
from minesweeper import decision

class BasicFunctionality(TestCase):
    def test__simplest_case(self):
        N = 1
        M = 1
        X = 1
        expected = False
        result = decision(M, N, X)
        self.assertEquals(expected, result)

    def test__1x2_1(self):
        N = 1
        M = 2
        X = 1
        expected = False
        result = decision(M, N, X)
        self.assertEquals(expected, result)

    def test__1x3_1(self):
        N = 1
        M = 3
        X = 1
        expected = True
        result = decision(M, N, X)
        self.assertEquals(expected, result)

    def test__1x3_3(self):
        N = 1
        M = 3
        X = 2
        expected = False
        result = decision(M, N, X)
        self.assertEquals(expected, result)

    def test__case_2x2_1(self):
        N = 2
        M = 2
        X = 1
        expected = False
        result = decision(M, N, X)
        self.assertEquals(expected, result)

    def test__case_2x2_2(self):
        N = 2
        M = 2
        X = 2
        expected = False
        result = decision(M, N, X)
        self.assertEquals(expected, result)

    def test__case_3x3_1(self):
        N = 3
        M = 3
        X = 1
        expected = True
        result = decision(M, N, X)
        self.assertEquals(expected, result)

    def test__case_3x3_5(self):
        N = 3
        M = 3
        X = 5
        expected = True
        result = decision(M, N, X)
        self.assertEquals(expected, result)

    def test__case_3x3_6(self):
        N = 3
        M = 3
        X = 6
        expected = False
        result = decision(M, N, X)
        self.assertEquals(expected, result)

    def test__case_3x4_8(self):
        N = 3
        M = 4
        X = 8
        expected = True
        result = decision(M, N, X)
        self.assertEquals(expected, result)
