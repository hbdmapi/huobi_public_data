#!/bin/bash
rm -rf *.txt

curl -s -H 'Content-Type: application/json'  https://api.huobi.pro/v1/common/symbols | jq -r '.data | sort_by(.symbol) | .[] | .symbol' > spot.txt

curl -s -H 'Content-Type: application/json'  https://api.hbdm.vn/api/v1/contract_contract_info | jq -r '.data | sort_by(.contract_code) | .[] | .contract_code' > futures.txt

curl -s -H 'Content-Type: application/json'  https://api.hbdm.vn/swap-api/v1/swap_contract_info | jq -r '.data | sort_by(.contract_code) | .[] | .contract_code' > swap.txt

curl -s -H 'Content-Type: application/json'  https://api.hbdm.vn/linear-swap-api/v1/swap_contract_info | jq -r '.data | sort_by(.contract_code) | .[] | select(.support_margin_mode == "all" or .support_margin_mode =="isolated") | .contract_code' > linear-swap-isolated.txt

curl -s -H 'Content-Type: application/json'  https://api.hbdm.vn/linear-swap-api/v1/swap_contract_info | jq -r '.data | sort_by(.contract_code) | .[] | select(.support_margin_mode == "all" or .support_margin_mode =="cross") | .contract_code' > linear-swap-cross.txt

curl -s -H 'Content-Type: application/json'  https://api.hbdm.vn/option-api/v1/option_contract_info | jq -r '.data | sort_by(.contract_code) | .[] | .contract_code' > options.txt
