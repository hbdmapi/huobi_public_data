from const import *
from utils import *
from download import *

data_type = 'klines'


def download_daily_spot(all_period: list = None, start: datetime = None, end: datetime = None, all_symbols: list = None):
    '''return date is: [start, end)'''

    global data_type
    b_download_daily_spot(data_type, all_period, start, end, all_symbols)


def download_daily_future(all_period: list = None, start: datetime = None, end: datetime = None, all_symbols: list = None):
    '''return date is: [start, end)'''

    global data_type
    b_download_daily_future(data_type, all_period, start, end, all_symbols)


def download_daily_swap(all_period: list = None, start: datetime = None, end: datetime = None, all_symbols: list = None):
    '''return date is: [start, end)'''

    global data_type
    b_download_daily_swap(data_type, all_period, start, end, all_symbols)


def download_daily_linearswap(all_period: list = None, start: datetime = None, end: datetime = None, all_symbols: list = None):
    '''return date is: [start, end)'''

    global data_type
    b_download_daily_linearswap(data_type, all_period, start, end, all_symbols)


def download_daily_option(all_period: list = None, start: datetime = None, end: datetime = None, all_symbols: list = None):
    '''return date is: [start, end)'''

    global data_type
    b_download_daily_option(data_type, all_period, start, end, all_symbols)


if __name__ == "__main__":
    download_daily_spot(all_symbols=['BTCUSDT', 'ADAUSDT'],
                        start=datetime(2021, 5, 21),
                        end=datetime(2021, 5, 23),
                        all_period=['1min', '15min'])
    #download_daily_future()
    #download_daily_swap()
    #download_daily_linearswap()
    #download_daily_option(all_period=['1min'])
