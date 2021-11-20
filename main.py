# imports
from datetime import datetime

from unittest import mock


# this function collects & tests user data for the queries-stock symbol, chart type, time series, start date & end date
def get_user_input():

    while True:
        try:  # testing user input
            stock_symbol = input('Enter the Stock Symbol you are looking for: ')
            stock_symbol = stock_symbol.upper()
            if stock_symbol == "":  # testing if user input is null
                print('Stock Symbol Example: GOOGL')    # input example due to null input
                raise Exception
            if len(stock_symbol) > 7:
                print('Stock Symbol must not exceed 7 characters...:')
                print('Stock Symbol Example: GOOGL')
                raise Exception
        except Exception:  # catching errors
            print('\nInvalid Entry. Please try again...')
            continue
        else:
            while True:
                try:  # testing user input
                    print('\nGraph Types\n------------\n1. Bar\n2. Line\n')
                    chart_type = int(input('Enter the Graph Type you want (1, 2): '))
                    if chart_type < 1 or chart_type > 2:
                        raise Exception
                except Exception:  # catching invalid input
                    print('\nInvalid entry: Please try again...')
                    continue
                else:
                    while True:
                        try:  # testing user input
                            print('\nTime Series\n-----------\n1. Intraday\n2. Daily\n3. Weekly\n4. Monthly\n')
                            time_series = int(input("Enter time series option (1, 2, 3, 4): "))
                            if time_series < 1 or time_series > 4:
                                raise Exception
                        except Exception:  # catching invalid input
                            print('\nInvalid entry: Please try again...')
                            continue
                        else:

                            while True:
                                try:  # testing user input on start date
                                    start_day = input('\nEnter the start date (YYYY-MM-DD): ')
                                    start_date_obj = datetime.strptime(start_day, "%Y-%m-%d")  # converting string input to date object and formmating
                                    start_date = start_date_obj.date()  # removing time from date object
                                except Exception:  # raising exception for date format error
                                    print('\nInvalid entry. Please try again...')
                                    continue
                                else:
                                    while True:  # starting another loop for end date
                                        try:  # testing user input on end date
                                            end_day = input('Enter the end date (YYYY-MM-DD): ')
                                            end_date_obj = datetime.strptime(end_day, "%Y-%m-%d")
                                            # converting string input to date object and formatting
                                            if end_date_obj <= start_date_obj:
                                            # raising exception if end date is before start date
                                                print('\nEnd Date must be after Start Date. Current Start Date is', start_date)  # informs user of error
                                                raise Exception
                                        except Exception:  # catching other error like date formats
                                            print('Invalid entry. Please try again...')
                                            continue
                                        else:
                                            end_date = end_date_obj.date()  # removing time from date object
                                            return stock_symbol, chart_type, time_series, start_date, end_date


def test_get_user_input():
    with mock.patch('builtins.input', lambda *args: ):
        assert get_user_input() == ['GOOGL', 1, 4, '2012-09-14', '2013-10-10']

    with mock.patch('builtins.input', return_value=['T', 2, 2, '2013-08-15', '2018-11-11']):
        assert get_user_input() == ['T', 2, 2, '2013-08-15', '2018-11-11']

    with mock.patch('builtins.input', return_value=['CMG', 1, 3, '2009-08-11', '2010-11-12']):
        assert get_user_input() == ['CMG', 1, 3, '2009-08-11', '2010-11-12']

    with mock.patch('builtins.input', return_value=['AAPL', 2, 4, '2020-01-03', '2021-01-03']):
        assert get_user_input() == ['AAPL', 2, 4, '2020-01-03', '2021-01-03']


test_get_user_input()
