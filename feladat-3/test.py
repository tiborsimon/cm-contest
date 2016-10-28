from unittest import TestCase
from main import decision

class BasicFunctionality(TestCase):
    def test__simplest_case(self):
        """
        *
        """
        N = 1
        M = 1
        X = 1
        expected = False
        result = decision(M, N, X)
        self.assertEquals(expected, result)

    def test__1x2_1(self):
        """
        1*
        """
        N = 1
        M = 2
        X = 1
        expected = False
        result = decision(M, N, X)
        self.assertEquals(expected, result)

    def test__1x3_1(self):
        """
        01*
        """
        N = 1
        M = 3
        X = 1
        expected = True
        result = decision(M, N, X)
        self.assertEquals(expected, result)

    def test__1x3_3(self):
        """
        1**
        """
        N = 1
        M = 3
        X = 2
        expected = False
        result = decision(M, N, X)
        self.assertEquals(expected, result)

    def test__case_2x2_1(self):
        """
        11
        1*
        """
        N = 2
        M = 2
        X = 1
        expected = False
        result = decision(M, N, X)
        self.assertEquals(expected, result)

    def test__case_2x2_2(self):
        """
        2*
        2*
        """
        N = 2
        M = 2
        X = 2
        expected = False
        result = decision(M, N, X)
        self.assertEquals(expected, result)

    def test__case_3x3_1(self):
        """
        000
        011
        01*
        """
        N = 3
        M = 3
        X = 1
        expected = True
        result = decision(M, N, X)
        self.assertEquals(expected, result)

    def test__case_3x3_5(self):
        """
        02*
        23*
        ***
        """
        N = 3
        M = 3
        X = 5
        expected = True
        result = decision(M, N, X)
        self.assertEquals(expected, result)

    def test__case_3x3_6(self):
        """
        13*
        3**
        ***
        """
        N = 3
        M = 3
        X = 6
        expected = False
        result = decision(M, N, X)
        self.assertEquals(expected, result)

    def test__case_3x4_8(self):
        """
        02**
        25**
        ****
        """
        N = 3
        M = 4
        X = 8
        expected = True
        result = decision(M, N, X)
        self.assertEquals(expected, result)

    def test__case_3x4_9(self):
        """
        13**
        3***
        ****
        """
        N = 3
        M = 4
        X = 9
        expected = False
        result = decision(M, N, X)
        self.assertEquals(expected, result)

    def test__case_5x5_16(self):
        """
        *****
        *333*
        *303*
        *333*
        *****
        """
        N = 5
        M = 5
        X = 16
        expected = True
        result = decision(M, N, X)
        self.assertEquals(expected, result)

    def test__case_5x5_17(self):
        """
        *****
        *333*
        *314*
        *34**
        *****
        """
        N = 5
        M = 5
        X = 17
        expected = False
        result = decision(M, N, X)
        self.assertEquals(expected, result)

