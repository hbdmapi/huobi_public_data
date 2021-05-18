from datetime import *

MONTHS = list(range(1,13))

SPOT_START_DATE = datetime(2017, 10, 27)
FUTURE_START_DATE = datetime(2018, 11, 10)
SWAP_START_DATE = datetime(2020, 3, 25)
LINEARSWAP_START_DATE = datetime(2020, 10, 21)
OPTION_START_DATE = datetime(2020, 9, 1)

END_DATE = datetime.now()

ALL_PERIODS = ['1min', '5min', '15min', '30min', '60min', '4hour', '1day']

BASE_URL = 'https://data.huobi.vision/data'

