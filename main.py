#! /usr/bin/python3

from time import time
from helping_functions import login_IQ_Option, consecutive_down, consecutive_up, write_consecutives
from all_tradeable_actives import all_tradeable_actives
from variables import expiration_mode

ACTIVE = input('Active: ').upper()
while ACTIVE not in all_tradeable_actives:
    ACTIVE = input('Active: ').upper()

TIMEFRAME = int(input('Timeframe (30, 60, 120 or 300): '))
while TIMEFRAME not in (30, 60, 120, 300):
    TIMEFRAME = int(input('Timeframe (30, 60, 120 or 300): '))

EXPIRATION_MODE = expiration_mode[str(TIMEFRAME)]

iqoption = login_IQ_Option()
check, reason = iqoption.connect()

BALANCE = iqoption.get_balance()

if check:
    loop = True
    arr = [0,0]
    while loop:
        candles = iqoption.get_candles(ACTIVE, TIMEFRAME, 6, time())
        current = candles[-1]
        last_candles = candles[:-1]

        if current['to'] not in arr:
            arr.append(current['to'])
            arr = arr[1:]

            if consecutive_up(last_candles): 
                write_consecutives(ACTIVE, 'UP')

            if consecutive_down(last_candles):
                write_consecutives(ACTIVE, 'DOWN')
        
