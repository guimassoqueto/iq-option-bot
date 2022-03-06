#! /usr/bin/python3

from time import time, sleep
from helping_functions import (
    login_IQ_Option, 
    consecutive_down, 
    consecutive_up, 
    all_tradeable_actives, 
    enter_operation, 
    trade_result
)

from variables import expiration_mode

all_act = all_tradeable_actives()

ACTIVE = input('Active: ').upper()
while ACTIVE not in all_act:
    ACTIVE = input('Active: ').upper()

TIMEFRAME = int(input('Timeframe (30, 60, 120 or 300): '))
while TIMEFRAME not in (30, 60, 120, 300):
    TIMEFRAME = int(input('Timeframe (30, 60, 120 or 300): '))

EXPIRATION = expiration_mode[str(TIMEFRAME)]

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
                loop = False
                action = 'put'
                status0, p0 = enter_operation(iqoption, ACTIVE, action, BALANCE, 0, EXPIRATION)

                if(status0 == 'loose'):
                    status1, p1 = enter_operation(iqoption, ACTIVE, action, BALANCE, 1, EXPIRATION)

                    if(status1 == 'loose'):
                        status2, p2 = enter_operation(iqoption, ACTIVE, action, BALANCE, 2, EXPIRATION)

                        if(status2 == 'loose'):
                            status3, p3 = enter_operation(iqoption, ACTIVE, action, BALANCE, 3, EXPIRATION)

                            if(status3 == 'loose'):
                                status4, p4 = enter_operation(iqoption, ACTIVE, action, BALANCE, 4, EXPIRATION)

                                if(status4 == 'loose'):
                                    status5, p5 = enter_operation(iqoption, ACTIVE, action, BALANCE, 5, EXPIRATION)

                                    if(status5 == 'loose'):
                                        status6, p6 = enter_operation(iqoption, ACTIVE, action, BALANCE, 6, EXPIRATION)

                                        if (status6 == 'loose'):
                                            sleep(600)
                                            loop, BALANCE = trade_result(iqoption, p6 + p5 + p4 + p3 + p2 + p1 + p0)
                                        else:
                                            loop, BALANCE = trade_result(iqoption, p6 + p5 + p4 + p3 + p2 + p1 + p0)
                                    else:
                                        loop, BALANCE = trade_result(iqoption, p5 + p4 + p3 + p2 + p1 + p0)
                                else:
                                    loop, BALANCE = trade_result(iqoption, p4 + p3 + p2 + p1 + p0)
                            else:
                                loop, BALANCE = trade_result(iqoption, p3 + p2 + p1 + p0)
                        else:
                            loop, BALANCE = trade_result(iqoption, p2 + p1 + p0)
                    else:
                        loop, BALANCE = trade_result(iqoption, p1 + p0)
                else:
                    loop, BALANCE = trade_result(iqoption, p0)

            if consecutive_down(last_candles):
                loop = False
                action = 'call'
                status0, p0 = enter_operation(iqoption, ACTIVE, action, BALANCE, 0, EXPIRATION)

                if(status0 == 'loose'):
                    status1, p1 = enter_operation(iqoption, ACTIVE, action, BALANCE, 1, EXPIRATION)

                    if(status1 == 'loose'):
                        status2, p2 = enter_operation(iqoption, ACTIVE, action, BALANCE, 2, EXPIRATION)

                        if(status2 == 'loose'):
                            status3, p3 = enter_operation(iqoption, ACTIVE, action, BALANCE, 3, EXPIRATION)

                            if(status3 == 'loose'):
                                status4, p4 = enter_operation(iqoption, ACTIVE, action, BALANCE, 4, EXPIRATION)

                                if(status4 == 'loose'):
                                    status5, p5 = enter_operation(iqoption, ACTIVE, action, BALANCE, 5, EXPIRATION)

                                    if(status5 == 'loose'):
                                        status6, p6 = enter_operation(iqoption, ACTIVE, action, BALANCE, 6, EXPIRATION)

                                        if (status6 == 'loose'):
                                            sleep(600)
                                            loop, BALANCE = trade_result(iqoption, p6 + p5 + p4 + p3 + p2 + p1 + p0)
                                        else:
                                            loop, BALANCE = trade_result(iqoption, p6 + p5 + p4 + p3 + p2 + p1 + p0)
                                    else:
                                        loop, BALANCE = trade_result(iqoption, p5 + p4 + p3 + p2 + p1 + p0)
                                else:
                                    loop, BALANCE = trade_result(iqoption, p4 + p3 + p2 + p1 + p0)
                            else:
                                loop, BALANCE = trade_result(iqoption, p3 + p2 + p1 + p0)
                        else:
                            loop, BALANCE = trade_result(iqoption, p2 + p1 + p0)
                    else:
                        loop, BALANCE = trade_result(iqoption, p1 + p0)
                else:
                    loop, BALANCE = trade_result(iqoption, p0)
        else: continue
