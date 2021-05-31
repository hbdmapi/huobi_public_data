import requests
from utils import *
from bs4 import BeautifulSoup

_url = 'http://huobi-service-data.s3-ap-northeast-1.amazonaws.com/'


def _get_s3_symbols(flag: str) -> tuple:
    global _url

    if flag is None:
        return False, None

    symbols = []
    url = f'{_url}?delimiter=/&prefix={flag}'
    response = requests.get(url)
    html = response.text.encode('utf-8')
    soup = BeautifulSoup(html, features="html.parser")
    cts = soup.select('CommonPrefixes')
    for ct in cts:
        key = ct.select('Prefix')[0].text
        if not key.startswith(flag):
            continue
        symbol = key[len(flag):]
        symbol = symbol[:symbol.find('/')]
        symbols.append(symbol)
    return True, symbols


def check_spot(s3_hb: bool = True):
    hok, hb_symbols = get_all_spot_symbols()
    if not hok:
        print('get symbols error')
        return

    sok, s3_symbols = _get_s3_symbols('data/klines/spot/daily/')
    if not sok:
        print('get symbols')
        return
    if s3_hb:
        out_symbols = set(s3_symbols) - set(hb_symbols)
    else:
        out_symbols = set(hb_symbols)-set(s3_symbols)
    print('spot klines symbols:')
    pd = filter(lambda x: not x.endswith('KRW'), out_symbols)
    print(set(pd))

    sok, s3_symbols = _get_s3_symbols('data/trades/spot/daily/')
    if not sok:
        print('check error')
        return
    if s3_hb:
        out_symbols = set(s3_symbols) - set(hb_symbols)
    else:
        out_symbols = set(hb_symbols)-set(s3_symbols)
    print('spot trades symbols:')
    pd = filter(lambda x: not x.endswith('KRW'), out_symbols)
    print(set(pd))


def check_future(s3_hb: bool = True):
    hok, hb_symbols = get_all_future_symbols()
    if not hok:
        print('get symbols error')
        return

    sok, s3_symbols = _get_s3_symbols('data/klines/future/daily/')
    if not sok:
        print('get symbols')
        return
    if s3_hb:
        out_symbols = set(s3_symbols) - set(hb_symbols)
    else:
        out_symbols = set(hb_symbols)-set(s3_symbols)
    print('future klines symbols:')
    print(out_symbols)

    sok, s3_symbols = _get_s3_symbols('data/trades/future/daily/')
    if not sok:
        print('check error')
        return
    if s3_hb:
        out_symbols = set(s3_symbols) - set(hb_symbols)
    else:
        out_symbols = set(hb_symbols)-set(s3_symbols)
    print('future trades symbols:')
    print(out_symbols)


def check_swap(s3_hb: bool = True):
    hok, hb_symbols = get_all_swap_symbols()
    if not hok:
        print('get symbols error')
        return

    sok, s3_symbols = _get_s3_symbols('data/klines/swap/daily/')
    if not sok:
        print('get symbols')
        return
    if s3_hb:
        out_symbols = set(s3_symbols) - set(hb_symbols)
    else:
        out_symbols = set(hb_symbols)-set(s3_symbols)
    print('swap klines symbols:')
    print(out_symbols)

    sok, s3_symbols = _get_s3_symbols('data/trades/swap/daily/')
    if not sok:
        print('check error')
        return
    if s3_hb:
        out_symbols = set(s3_symbols) - set(hb_symbols)
    else:
        out_symbols = set(hb_symbols)-set(s3_symbols)
    print('swap trades symbols:')
    print(out_symbols)


def check_linearswap(s3_hb: bool = True):
    hok, hb_symbols = get_all_linearswap_symbols()
    if not hok:
        print('get symbols error')
        return

    sok, s3_symbols = _get_s3_symbols('data/klines/linearswap/daily/')
    if not sok:
        print('get symbols')
        return
    if s3_hb:
        out_symbols = set(s3_symbols) - set(hb_symbols)
    else:
        out_symbols = set(hb_symbols)-set(s3_symbols)
    print('linearswap klines symbols:')
    print(out_symbols)

    sok, s3_symbols = _get_s3_symbols('data/trades/linearswap/daily/')
    if not sok:
        print('check error')
        return
    if s3_hb:
        out_symbols = set(s3_symbols) - set(hb_symbols)
    else:
        out_symbols = set(hb_symbols)-set(s3_symbols)
    print('linearswap trades symbols:')
    print(out_symbols)


def check_option(s3_hb: bool = True):
    hok, hb_symbols = get_all_option_symbols()
    if not hok:
        print('get symbols error')
        return

    sok, s3_symbols = _get_s3_symbols('data/klines/option/daily/')
    if not sok:
        print('get symbols')
        return
    if s3_hb:
        out_symbols = set(s3_symbols) - set(hb_symbols)
    else:
        out_symbols = set(hb_symbols)-set(s3_symbols)
    print('option klines symbols:')
    print(out_symbols)

    sok, s3_symbols = _get_s3_symbols('data/trades/option/daily/')
    if not sok:
        print('check error')
        return
    if s3_hb:
        out_symbols = set(s3_symbols) - set(hb_symbols)
    else:
        out_symbols = set(hb_symbols)-set(s3_symbols)
    print('option trades symbols:')
    print(out_symbols)


if __name__ == '__main__':
    check_spot()
    check_future()
    check_swap()
    check_linearswap()
    check_option()
