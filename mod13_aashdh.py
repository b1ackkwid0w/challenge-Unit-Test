import unittest
import datetime


class TestGetUserInput(unittest.TestCase):

    def test_stock_symbol(get_user_input):
        stock_symbol = 'IBM'
        get_user_input.assertLess(len(stock_symbol), 7, msg="stock symbol more than 7 char")
        get_user_input.assertGreater(len(stock_symbol), 1, msg="stock symbol less than 1 char")
        get_user_input.assertTrue(stock_symbol.isupper(), msg="stock symbol is lowercase")

    def test_chart_type(get_user_input):
        chart_type = 1
        get_user_input.assertLessEqual(chart_type, 2, msg="chart type more than 2")
        get_user_input.assertGreaterEqual(chart_type, 1, msg="chart type less than 1")
        get_user_input.assertTrue(type(chart_type) == int, msg="chart type not numeric")

    def test_time_series(get_user_input):
        time_series = 1
        get_user_input.assertLessEqual(time_series, 4, msg="time series  more than 4")
        get_user_input.assertGreaterEqual(time_series, 1, msg="time series less than 1")
        get_user_input.assertTrue(type(time_series) == int, msg="time series not numeric")

    def test_start_date(get_user_input):
        start_date = datetime.datetime.strptime("2012-09-14", "%Y-%m-%d").date()
        test_date = datetime.date
        get_user_input.assertIsInstance(start_date, test_date, msg="start date is not a date object")

    def test_end_date(get_user_input):
        end_date = datetime.datetime.strptime("2012-09-14", "%Y-%m-%d").date()
        test_date = datetime.date
        get_user_input.assertIsInstance(end_date, test_date, msg="end date is not a date object")


if __name__ == '__main__':
    unittest.main()
