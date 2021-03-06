#!/bin/bash

pre_url="https://futures.huobi.com/data/klines"

downlowd_daily(){
  d_type=$1 # such as spot/future/swap/linear-swap/option
  all_symbols=$2 # such as HTUSDT,BTCUSDT
  all_periods=$3 # such as 1min,5min,15min,30min,60min,4hour,1day
  all_years=$4 # such as 2019,2020,2021
  all_months=$5 # such as 01,02,03,04,05,06,07,08,09,10,11,12
  all_days=$6 #such as 01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31

  # to list
  all_symbols=(${all_symbols//,/ }) 
  all_periods=(${all_periods//,/ }) 
  all_years=(${all_years//,/ }) 
  all_months=(${all_months//,/ }) 
  all_days=(${all_days//,/ }) 

  for d_symbol in ${all_symbols[@]}
  do
    for d_period in ${all_periods[@]}
    do
      for d_year in ${all_years[@]}
      do
        for d_month in ${all_months[@]}
        do
          for d_day in ${all_days[@]}
          do
            url="${pre_url}/${d_type}/daily/${d_symbol}/${d_period}/${d_symbol}-${d_period}-${d_year}-${d_month}-${d_day}"
            # echo $url
            zip_file="${url}.zip"
            check_file="${url}.CHECKSUM"

            $(curl -# -O ${zip_file})
            $(curl -# -O ${check_file})
          done
        done
      done
    done
  done
}

downlowd_monthly(){
  d_type=$1 # such as spot/future/swap/linear-swap/option
  all_symbols=$2 # such as HTUSDT,BTCUSDT
  all_periods=$3 # such as 1min,5min,15min,30min,60min,4hour,1day
  all_years=$4 # such as 2019,2020,2021
  all_months=$5 # such as 01,02,03,04,05,06,07,08,09,10,11,12

  # to list
  all_symbols=(${all_symbols//,/ }) 
  all_periods=(${all_periods//,/ }) 
  all_years=(${all_years//,/ }) 
  all_months=(${all_months//,/ }) 

  for d_symbol in ${all_symbols[@]}
  do
    for d_period in ${all_periods[@]}
    do
      for d_year in ${all_years[@]}
      do
        for d_month in ${all_months[@]}
        do
          url="${pre_url}/${d_type}/monthly/${d_symbol}/${d_period}/${d_symbol}-${d_period}-${d_year}-${d_month}"
          zip_file="${url}.zip"
          check_file="${url}.CHECKSUM"

          $(curl -# -O ${zip_file})
          $(curl -# -O ${check_file})
        done
      done
    done
  done
}

# ----------------------------------------------------------------------------
# test functions]
test_daily(){
  downlowd_daily spot ADAUSDT,BTCUSDT 1min,5min 2021 05 21,23
}

test_monthly(){
  downlowd_monthly spot ADAUSDT,BTCUSDT 1min,5min 2020,2021 01,02
}

# ----------------------------------------------------------------------------
# run
test_daily
# test_monthly