
from unittest import TestCase
from .. import app

class ValidNumberTest(TestCase):

    ERROR_MSG = 'Invalid - `%s`'

    def setUp(self):
        self.solution = app.Solution()
        
    ### sample input from leetcode
    def test_number(self):
        test_str = '0'
        self.assertTrue(expr=self.solution.isNumber(test_str), 
            msg=ValidNumberTest.ERROR_MSG%(test_str))

    def test_float_number(self):
        test_str = ' 0.1'
        self.assertTrue(expr=self.solution.isNumber(test_str), 
            msg=ValidNumberTest.ERROR_MSG%(test_str))

    def test_alphabet(self):
        test_str = 'abc'
        self.assertTrue(expr=not self.solution.isNumber(test_str), 
            msg=ValidNumberTest.ERROR_MSG%(test_str))

    def test_number_with_alphabet(self):
        test_str = '1 a'
        self.assertTrue(expr=not self.solution.isNumber(test_str), 
            msg=ValidNumberTest.ERROR_MSG%(test_str))

    def test_exponent(self):
        test_str = '2e10'
        self.assertTrue(expr=self.solution.isNumber(test_str), 
            msg=ValidNumberTest.ERROR_MSG%(test_str))

    def test_exponent2(self):
        test_str = '2e10e'
        self.assertTrue(expr=not self.solution.isNumber(test_str), 
            msg=ValidNumberTest.ERROR_MSG%(test_str))

    def test_wrong1(self):
        test_str = 'e9'
        self.assertTrue(expr=not self.solution.isNumber(test_str), 
            msg=ValidNumberTest.ERROR_MSG%(test_str))

    def test_wrong2(self):
        test_str = '.1'
        self.assertTrue(expr=self.solution.isNumber(test_str), 
            msg=ValidNumberTest.ERROR_MSG%(test_str))

    def test_wrong3(self):
        test_str = '3.'
        self.assertTrue(expr=self.solution.isNumber(test_str), 
            msg=ValidNumberTest.ERROR_MSG%(test_str))

    def test_wrong4(self):
        test_str = '0e'
        self.assertTrue(expr=not self.solution.isNumber(test_str), 
            msg=ValidNumberTest.ERROR_MSG%(test_str))

    def test_wrong5(self):
        test_str = '46.e3'
        self.assertTrue(expr=self.solution.isNumber(test_str), 
            msg=ValidNumberTest.ERROR_MSG%(test_str))

    def test_wrong6(self):
        test_str = '.e'
        self.assertTrue(expr=not self.solution.isNumber(test_str), 
            msg=ValidNumberTest.ERROR_MSG%(test_str))

    def test_wrong7(self):
        test_str = '.e1'
        self.assertTrue(expr=not self.solution.isNumber(test_str), 
            msg=ValidNumberTest.ERROR_MSG%(test_str))

    def test_wrong8(self):
        test_str = '0.e'
        self.assertTrue(expr=not self.solution.isNumber(test_str), 
            msg=ValidNumberTest.ERROR_MSG%(test_str))

    def test_wrong9(self):
        test_str = '6e6.5'
        self.assertTrue(expr=not self.solution.isNumber(test_str), 
            msg=ValidNumberTest.ERROR_MSG%(test_str))

    def test_wrong10(self):
        test_str = ' 005047e+6'
        self.assertTrue(expr=self.solution.isNumber(test_str), 
            msg=ValidNumberTest.ERROR_MSG%(test_str))

    def test_wrong11(self):
        test_str = '3.5e+3.5e+3.5'
        self.assertTrue(expr=not self.solution.isNumber(test_str), 
            msg=ValidNumberTest.ERROR_MSG%(test_str))
