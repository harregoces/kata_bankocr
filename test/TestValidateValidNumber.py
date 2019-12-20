import unittest
import sys
sys.path.append("../src/")
import ValidateNumber


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.number_to_test = '345882865'

    def test_validate_number(self):
        validate_number = ValidateNumber()
        result = validate_number.validate_number(self.number_to_test)
        self.assertEqual(True, result)


if __name__ == '__main__':
    unittest.main()
