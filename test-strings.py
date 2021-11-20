# test suite
import unittest


class TestStringMethods(unittest.TestCase):

    # positive test function to test if values
    # are almost equal with place
    def test_positiveForGreater(self):
        first = 4
        second = 3

        # error message in case if test case got failed
        message = "first value is not greater that second value."

        # assert function() to check if values1 is
        # greater than value2
        self.assertGreater(first, second, message)


if __name__ == '__main__':
    unittest.main()
