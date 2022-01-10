#! /usr/bin/python3

from time import time
from helping_functions import login_IQ_Option, write_delay
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
    arr = []
    while loop:
        last_two = iqoption.get_candles(ACTIVE, TIMEFRAME, 3, time())
        [c2, c1, c0] = last_two

        if c0['to'] not in arr: 
            arr.clear()
            arr.append(c0['to'])

            if c2['open'] < c2['close'] and c1['open'] < c1['close']:
                loop = False
                action = 'put'
                start = time()
                success, id = iqoption.buy(BALANCE * 0.0001, ACTIVE, action, EXPIRATION_MODE)

                while not success:
                    success, id = iqoption.buy(BALANCE * 0.0001, ACTIVE, action, EXPIRATION_MODE)

                end = time()

                write_delay(ACTIVE, TIMEFRAME, action, end - start)

                status, profit = iqoption.check_win_v3(id)
                loop = True       

            elif c2['open'] > c2['close'] and c1['open'] > c1['close']:
                loop = False
                action = 'call'
                start = time()
                success, id = iqoption.buy(BALANCE * 0.0001, ACTIVE, action, EXPIRATION_MODE)

                while not success:
                    success, id = iqoption.buy(BALANCE * 0.0001, ACTIVE, action, EXPIRATION_MODE)

                end = time()

                write_delay(ACTIVE, TIMEFRAME, action, end - start)

                status, profit = iqoption.check_win_v3(id)
                loop = True

            else:
                continue

        else:
            continue
