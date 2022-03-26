#! /usr/bin/bash


#OTC=('AUDCAD-OTC' 'EURGBP-OTC' 'EURJPY-OTC' 'EURUSD-OTC' 'GBPJPY-OTC' 'GBPUSD-OTC' 'NZDUSD-OTC' 'USDCHF-OTC' 'USDHKD-OTC' 'USDINR-OTC' 'USDJPY-OTC' 'USDSGD-OTC' 'USDZAR-OTC')

REAL=('AUDCAD' 'EURGBP' 'EURJPY' 'EURUSD' 'GBPJPY' 'GBPUSD' 'NZDUSD' 'USDCHF' 'USDJPY')

for ACTIVE in ${REAL[@]};
do
	/home/guilherme/Desktop/iq-option-bot/helpers/probability_v2.py $ACTIVE 60 100 1>> /home/guilherme/Desktop/prob/$ACTIVE.txt;
done;


