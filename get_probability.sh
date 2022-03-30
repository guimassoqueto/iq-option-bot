#! /usr/bin/bash


#OTC=('AUDCAD-OTC' 'EURGBP-OTC' 'EURJPY-OTC' 'EURUSD-OTC' 'GBPJPY-OTC' 'GBPUSD-OTC' 'NZDUSD-OTC' 'USDCHF-OTC' 'USDHKD-OTC' 'USDINR-OTC' 'USDJPY-OTC' 'USDSGD-OTC' 'USDZAR-OTC')

REAL=('EURGBP' 'EURJPY' 'EURUSD' 'EURGBP-OTC' 'EURJPY-OTC' 'EURUSD-OTC')

for ACTIVE in ${REAL[@]};
do
	/home/guilherme/Desktop/iq-option-bot/helpers/probability_v2.py $ACTIVE 60 1 1> /home/guilherme/Desktop/prob/$ACTIVE.txt;

done;


