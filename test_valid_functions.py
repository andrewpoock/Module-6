from more_functions import validate_functions
import unittest


class TestStringMethods(unittest.TestCase):
    def test_name(self):
        try:
            print(validate_functions.score_input('Test'))
        except ValueError as err:
            print("ValueError encountered")

    def test_valid(self):
        self.assertEqual(validate_functions.score_input('Test', 30, 'input not valid'), 'Test: 30')

    def test_below(self):
        with self.assertRaises(ValueError):
            validate_functions.score_input('Test', -5, 'input not valid')

    def test_above(self):
        with self.assertRaises(ValueError):
            validate_functions.score_input('Test', 110, 'input not valid')

    def test_other(self):
        with self.assertRaises(ValueError):
            validate_functions.score_input('Test', 'ss', 'input not valid')

    def test_invalid_message(self):
        try:
            print(validate_functions.score_input('Test', 30, 'input not valid'))
        except ValueError as err:
            print("ValueError encountered")


if __name__ == '__main__':
    unittest.main()
