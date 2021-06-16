import requests
import os
from const import *
from datetime import timedelta
import json

just_show = False


def http_download(url: str) -> tuple:
  global just_show
  try:
    if url is None:
      return False, 'url is null'
    data = requests.get(url, allow_redirects=True)
    if just_show:
      print(f'{file_name}<---{url}')
    else:
      file_name = os.path.basename(url)
      with open(file_name, 'wb') as f:
        f.write(data.content)
  except Exception as e:
    return False, str(e)
  return True, None


def http_get(url: str, params: dict = None, headers: dict = None) -> tuple:
  try:
    if headers is None:
      headers = {'Content-type': 'application/x-www-form-urlencoded'}
    res = requests.get(url, params=params, headers=headers)
    data = res.json()
  except Exception as e:
      return False, str(e)
  return True, data


def get_all_spot_symbols() -> tuple:
  url = 'https://api.huobi.pro/v1/common/symbols'
  ok, data = http_get(url)
  if not ok:
    return ok, data
  if data['status'] != 'ok':
    return False, data['err-msg']
  result = []
  for item in data['data']:
    result.append(item['symbol'].upper())
  return True, result


def get_all_future_symbols() -> tuple:
  url = 'https://api.hbdm.com/api/v1/contract_contract_info'
  ok, data = http_get(url)
  if not ok:
    return ok, data
  if data['status'] != 'ok':
    return False, data['err_msg']
  all_symbols = []
  for item in data['data']:
    if item['symbol'] not in all_symbols:
      all_symbols.append(item['symbol'])

  result = []
  for symbol in all_symbols:
    url = 'https://futures.huobi.com/contract-order/x/v1/contract_delivery_detail'
    params = {'symbol': symbol, 'page_index': 1, 'page_size': 100}
    headers = {'source': 'web',
               'Content-Type': 'application/json; charset=UTF-8'}
    ok, data = http_get(url, params, headers)
    if not ok:
      return ok, data
    if data['status'] != 'ok':
      return False, data['err_msg']
    all_delivery = data['data']['delivery']
    for delivery in all_delivery:
      for insi in delivery['instrument_info']:
        contract_code = insi['contract_code']
        if contract_code not in result:
            result.append(contract_code)
    cp = data['data']['current_page']
    tp = data['data']['total_page']
    while cp < tp:
      cp = cp+1
      params = {'symbol': symbol, 'page_index': cp, 'page_size': 100}
      ok, i_data = http_get(url, params, headers)
      if not ok:
        return ok, i_data
      if i_data['status'] != 'ok':
        return False, i_data['err_msg']
      iad = i_data['data']['delivery']
      for delivery in iad:
        for insi in delivery['instrument_info']:
          contract_code = insi['contract_code']
          if contract_code not in result:
              result.append(contract_code)
      cp = i_data['data']['current_page']
      tp = i_data['data']['total_page']
  return True, result


def get_all_swap_symbols() -> tuple:
  url = 'https://api.hbdm.com/swap-api/v1/swap_contract_info'
  ok, data = http_get(url)
  if not ok:
    return ok, data
  if data['status'] != 'ok':
    return False, data['err_msg']
  result = []
  for item in data['data']:
    result.append(item['contract_code'])
  return True, result


def get_all_linearswap_symbols() -> tuple:
  url = 'https://api.hbdm.com/linear-swap-api/v1/swap_contract_info'
  ok, data = http_get(url)
  if not ok:
    return ok, data
  if data['status'] != 'ok':
    return False, data['err_msg']
  result = []
  for item in data['data']:
    result.append(item['contract_code'])
  return True, result


def get_all_option_symbols() -> tuple:
  url = 'https://api.hbdm.com/option-api/v1/option_contract_info'
  ok, data = http_get(url)
  if not ok:
    return ok, data
  if data['status'] != 'ok':
    return False, data['err_msg']
  all_symbols = []
  for item in data['data']:
    if item['symbol'] not in all_symbols:
      all_symbols.append(item['symbol'])

  result = []
  for symbol in all_symbols:
    url = 'https://futures.huobi.com/option-order/x/v1/option_delivery_detail'
    params = {'symbol': symbol, 'page_index': 1, 'page_size': 100}
    headers = {'source': 'web',
               'Content-Type': 'application/json; charset=UTF-8'}
    ok, data = http_get(url, params, headers)
    if not ok:
      return ok, data
    if data['status'] != 'ok':
      return False, data['err_msg']
    all_delivery = data['data']['delivery']
    for delivery in all_delivery:
      for insi in delivery['instrument_info']:
        contract_code = insi['contract_code']
        if contract_code not in result:
            result.append(contract_code)
    cp = data['data']['current_page']
    tp = data['data']['total_page']
    while cp < tp:
      cp = cp+1
      params = {'symbol': symbol, 'page_index': cp, 'page_size': 100}
      ok, i_data = http_get(url, params, headers)
      if not ok:
        return ok, i_data
      if i_data['status'] != 'ok':
        return False, i_data['err_msg']
      iad = i_data['data']['delivery']
      for delivery in iad:
        for insi in delivery['instrument_info']:
          contract_code = insi['contract_code']
          if contract_code not in result:
              result.append(contract_code)
      cp = i_data['data']['current_page']
      tp = i_data['data']['total_page']
  return True, result


def download_daily(path_url, symbol, period, start_date, end_date) -> tuple:
  all_oks = []
  all_errs = []
  interval = end_date-start_date
  for index in range(interval.days):
    current = start_date+timedelta(days=index)
    url = f'{path_url}/{symbol.upper()}-{period}-{current.year}-{current.month:02}-{current.day:02}'
    zip_file = f'{url}.zip'
    # print(zip_file)
    check_file = f'{url}.CHECKSUM'
    ok, msg = http_download(zip_file)
    if not ok:
      all_errs.append({'url': url, 'msg': msg})
    else:
      all_oks.append(zip_file)
    ok, msg = http_download(check_file)
    if not ok:
      all_errs.append({'url': url, 'msg': msg})
    else:
      all_oks.append(url)
  return all_oks, all_errs


def download_monthly(path_url, symbol, period, start_date, end_date) -> tuple:
  all_oks = []
  all_errs = []
  interval = end_date-start_date
  for index in range(interval.days):
    current = start_date+timedelta(days=index)
    url = f'{path_url}/{symbol.upper()}-{period}-{current.year}-{current.month:02}'
    zip_file = f'{url}.zip'
    check_file = f'{url}.CHECKSUM'
    ok, msg = http_download(zip_file)
    if not ok:
      all_errs.append({'url': url, 'msg': msg})
    else:
      all_oks.append(zip_file)
    ok, msg = http_download(check_file)
    if not ok:
      all_errs.append({'url': url, 'msg': msg})
    else:
      all_oks.append(url)
  return all_oks, all_errs


if __name__ == "__main__":
    print(get_all_spot_symbols())
    print(get_all_future_symbols())
    print(get_all_swap_symbols())
    print(get_all_linearswap_symbols())
    print(get_all_option_symbols())
