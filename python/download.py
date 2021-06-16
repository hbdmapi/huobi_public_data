from const import *
from utils import *

pre_url = "https://futures.huobi.com/data"


def b_download_daily_spot(data_type: str, all_period: list = None, start: datetime = None, end: datetime = None, all_symbols: list = None):
    '''return date is: [start, end)'''

    global pre_url
    if all_period is None:
        all_period = ALL_PERIODS
    if start is None:
        start = SPOT_START_DATE
    if end is None:
        end = END_DATE

    if all_symbols is None:
        ok, all_symbols = get_all_spot_symbols()
        if not ok:
            print(all_symbols)
            return
    for symbol in all_symbols:
        for period in all_period:
            if period in ['trades',]:
                path_url = f'{pre_url}/{data_type}/spot/daily/{symbol}'
            else:
                path_url = f'{pre_url}/{data_type}/spot/daily/{symbol}/{period}'
            all_oks, all_errs = download_daily(
                path_url, symbol, period, start, end)
            print(f'success:{all_oks}')
            print(f'faild:{all_errs}')
    print('done')


def b_download_daily_future(data_type: str, all_period: list = None, start: datetime = None, end: datetime = None, all_symbols: list = None):
    '''return date is: [start, end)'''

    global pre_url
    if all_period is None:
        all_period = ALL_PERIODS
    if start is None:
        start = SPOT_START_DATE
    if end is None:
        end = END_DATE

    if all_symbols is None:
        ok, all_symbols = get_all_future_symbols()
        if not ok:
            print(all_symbols)
            return
    for symbol in all_symbols:
        for period in all_period:
            if period in ['trades',]:
                path_url = f'{pre_url}/{data_type}/future/daily/{symbol}'
            else:
                path_url = f'{pre_url}/{data_type}/future/daily/{symbol}/{period}'
            all_oks, all_errs = download_daily(
                path_url, symbol, period, start, end)
            print(f'success:{all_oks}')
            print(f'faild:{all_errs}')
    print('done')


def b_download_daily_swap(data_type: str, all_period: list = None, start: datetime = None, end: datetime = None, all_symbols: list = None):
    '''return date is: [start, end)'''

    global pre_url
    if all_period is None:
        all_period = ALL_PERIODS
    if start is None:
        start = SPOT_START_DATE
    if end is None:
        end = END_DATE

    if all_symbols is None:
        ok, all_symbols = get_all_swap_symbols()
        if not ok:
            print(all_symbols)
            return
    for symbol in all_symbols:
        for period in all_period:
            if period in ['trades',]:
                path_url = f'{pre_url}/{data_type}/swap/daily/{symbol}'
            else:
                path_url = f'{pre_url}/{data_type}/swap/daily/{symbol}/{period}'
            all_oks, all_errs = download_daily(
                path_url, symbol, period, start, end)
            print(f'success:{all_oks}')
            print(f'faild:{all_errs}')
    print('done')


def b_download_daily_linearswap(data_type: str, all_period: list = None, start: datetime = None, end: datetime = None, all_symbols: list = None):
    '''return date is: [start, end)'''

    global pre_url
    if all_period is None:
        all_period = ALL_PERIODS
    if start is None:
        start = SPOT_START_DATE
    if end is None:
        end = END_DATE

    if all_symbols is None:
        ok, all_symbols = get_all_linearswap_symbols()
        if not ok:
            print(all_symbols)
            return
    for symbol in all_symbols:
        for period in all_period:
            if period in ['trades',]:
                path_url = f'{pre_url}/{data_type}/linear-swap/daily/{symbol}'
            else:
                path_url = f'{pre_url}/{data_type}/linear-swap/daily/{symbol}/{period}'
            all_oks, all_errs = download_daily(
                path_url, symbol, period, start, end)
            print(f'success:{all_oks}')
            print(f'faild:{all_errs}')
    print('done')


def b_download_daily_option(data_type: str, all_period: list = None, start: datetime = None, end: datetime = None, all_symbols: list = None):
    '''return date is: [start, end)'''

    global pre_url
    if all_period is None:
        all_period = ALL_PERIODS
    if start is None:
        start = SPOT_START_DATE
    if end is None:
        end = END_DATE

    if all_symbols is None:
        ok, all_symbols = get_all_option_symbols()
        if not ok:
            print(all_symbols)
            return
    for symbol in all_symbols:
        for period in all_period:
            if period in ['trades',]:
                path_url = f'{pre_url}/{data_type}/option/daily/{symbol}'
            else:
                path_url = f'{pre_url}/{data_type}/option/daily/{symbol}/{period}'
            all_oks, all_errs = download_daily(
                path_url, symbol, period, start, end)
            print(f'success:{all_oks}')
            print(f'faild:{all_errs}')
    print('done')
