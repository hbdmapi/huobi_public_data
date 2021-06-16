from const import *
from utils import *
from download import *

data_type = 'trades'


def download_daily_spot(start: datetime = None, end: datetime = None, all_symbols: list = None):
    '''return date is: [start, end)'''

    global data_type
    b_download_daily_spot(data_type, ['trades'], start, end, all_symbols)


def download_daily_future(start: datetime = None, end: datetime = None, all_symbols: list = None):
    '''return date is: [start, end)'''

    global data_type
    b_download_daily_future(data_type, ['trades'], start, end, all_symbols)


def download_daily_swap(start: datetime = None, end: datetime = None, all_symbols: list = None):
    '''return date is: [start, end)'''

    global data_type
    b_download_daily_swap(data_type, ['trades'], start, end, all_symbols)


def download_daily_linearswap(start: datetime = None, end: datetime = None, all_symbols: list = None):
    '''return date is: [start, end)'''

    global data_type
    b_download_daily_linearswap(data_type, ['trades'], start, end, all_symbols)


def download_daily_option(start: datetime = None, end: datetime = None, all_symbols: list = None):
    '''return date is: [start, end)'''

    global data_type
    b_download_daily_option(data_type, ['trades'], start, end, all_symbols)


if __name__ == "__main__":
    download_daily_spot(all_symbols=['btcusdt', 'ltcusdt'],
                        start=datetime(2021, 1, 1),
                        end=datetime(2021, 2, 1))
    #download_daily_future()
    #download_daily_swap()
    #download_daily_linearswap()
    #download_daily_option()
