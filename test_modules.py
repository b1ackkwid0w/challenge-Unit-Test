import unittest


class TestGetUserInput(unittest.TestCase):

    def test_stock_symbol(self):
        expected = "googl"
        actual = "GOOGL"
        self.assertTrue(expected, actual.isalpha(), msg="PASS")
        self.assertTrue(expected, actual.isupper(), msg="PASS")
        self.assertEqual(expected.upper(), actual, msg="PASS")
        self.assertLess(len(expected), len(actual), msg="FAIL")
        self.assertGreater(len(expected), len(actual), msg="FAIL")
        self.assertEqual(len(expected), len(actual), msg="PASS")

    def test_chart_type(self):
        expected = 1;
        actual = 1;
        self.assertTrue(expected, actual.isnumeric(), msg="PASS")
        self.assertEqual(expected, actual, msg="PASS")
        self.assertLess(expected, actual, msg="FAIL")
        self.assertGreater(expected, actual, msg="FAIL")

    def test_time_series(self):
        expected = 1;
        actual = 1;
        self.assertTrue(expected, actual.isnumeric(), msg="PASS")
        self.assertEqual(expected, actual, msg="PASS")
        self.assertLess(expected, actual, msg="FAIL")
        self.assertGreater(expected, actual, msg="FAIL")

    def test_start_date(self):
        expected = "%YYYY-%mm-%dd"
        actual = "2012-09-14"
        self.assertEqual(expected, actual, msg="PASS")

    def test_end_date(self):
        expected = "%YYYY-%mm-%dd"
        actual = "2012-09-14"
        self.assertEqual(expected, actual, msg="PASS")

if __name__ == '__main__':
    unittest.main()
