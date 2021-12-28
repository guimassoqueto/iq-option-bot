#! /usr/bin/python3

from time import time
from helpers import consecutive_up, consecutive_down, login_IQ_Option

iqoption = login_IQ_Option()
check,reason = iqoption.connect()

ACTIVES = input('Pair: ').upper()
BALANCE = iqoption.get_balance()

loop = True
# id, from, at, to, open, close, min, max, volume
if check:
    while loop:
        last_six = iqoption.get_candles(ACTIVES, 60, 6, time())
        [c5, c4, c3, c2, c1, c0] = last_six
        if c0['to'] == round(time()):
            if consecutive_down(last_six):
                loop = False              
                success, id = iqoption.buy(BALANCE * 0.005, ACTIVES, 'call', 1)
                entry_time = time()

                if success: 
                    status, profit = iqoption.check_win_v3(id)
                    if status == 'loose':
                        success, id = iqoption.buy(BALANCE * 0.01, ACTIVES, 'call', 1)
                        if success: 
                            status, profit = iqoption.check_win_v3(id)
                            if status == 'loose':
                                success, id = iqoption.buy(BALANCE * 0.02, ACTIVES, 'call', 1)
                                if success: 
                                    status, profit = iqoption.check_win_v3(id)
                                    if status == 'loose':
                                        BALANCE = iqoption.get_balance()
                                        print(f"Lose ${profit}")
                                        loop = True
                                        continue
                                    else: 
                                        BALANCE = iqoption.get_balance()
                                        print(f"Win ${profit}")
                                        loop = True
                                        continue
                            else: 
                                BALANCE = iqoption.get_balance()
                                print(f"Win ${profit}")
                                loop = True
                                continue
                    else: 
                        BALANCE = iqoption.get_balance()
                        print(f"Win ${profit}")
                        loop = True
                        continue
            elif consecutive_up(last_six):
                loop = False
                success, id = iqoption.buy(BALANCE * 0.005, ACTIVES, 'put', 1)
                entry_time = time()
                
                if success: 
                    status, profit = iqoption.check_win_v3(id)
                    if status == 'loose':
                        success, id = iqoption.buy(BALANCE * 0.01, ACTIVES, 'put', 1)
                        entry_time = time()
                        if success: 
                            status, profit = iqoption.check_win_v3(id)
                            if status == 'loose':
                                success, id = iqoption.buy(BALANCE * 0.02, ACTIVES, 'put', 1)
                                entry_time = time()
                                if success: 
                                    status, profit = iqoption.check_win_v3(id)
                                    if status == 'loose':
                                        BALANCE = iqoption.get_balance()
                                        print(f"Lose ${profit}")
                                        loop = True
                                        continue
                                    else: 
                                        BALANCE = iqoption.get_balance()
                                        print(f"Win ${profit}")
                                        loop = True
                                        continue
                            else: 
                                BALANCE = iqoption.get_balance()
                                print(f"Win ${profit}")
                                loop = True
                                continue
                    else: 
                        BALANCE = iqoption.get_balance()
                        print(f"Win ${profit}")
                        loop = True
                        continue
            else: continue