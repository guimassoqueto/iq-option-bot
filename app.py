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
        last_six = iqoption.get_candles(ACTIVES, 300, 6, time())
        [c5, c4, c3, c2, c1, c0] = last_six
        if c0['to'] == round(time()):
            if consecutive_down(last_six):
                loop = False              
                success, id = iqoption.buy(BALANCE * 0.01, ACTIVES, 'call', 5)
                entry_time = time()

                if success: 
                    status1, profit1 = iqoption.check_win_v3(id)
                    if status1 == 'loose':
                        success, id = iqoption.buy(BALANCE * 0.02, ACTIVES, 'call', 5)
                        if success: 
                            status2, profit2 = iqoption.check_win_v3(id)
                            if status2 == 'loose':
                                success, id = iqoption.buy(BALANCE * 0.04, ACTIVES, 'call', 5)
                                if success: 
                                    status3, profit3 = iqoption.check_win_v3(id)
                                    if status3 == 'loose':
                                        BALANCE = iqoption.get_balance()
                                        print(f"Lose ${profit1 + profit2 + profit3}")
                                        loop = True
                                        continue
                                    else: 
                                        BALANCE = iqoption.get_balance()
                                        print(f"Win ${profit3}")
                                        loop = True
                                        continue
                            else: 
                                BALANCE = iqoption.get_balance()
                                print(f"Win ${profit2}")
                                loop = True
                                continue
                    else: 
                        BALANCE = iqoption.get_balance()
                        print(f"Win ${profit1}")
                        loop = True
                        continue
            elif consecutive_up(last_six):
                loop = False
                success, id = iqoption.buy(BALANCE * 0.01, ACTIVES, 'put', 5)
                entry_time = time()
                
                if success: 
                    status1, profit1 = iqoption.check_win_v3(id)
                    if status1 == 'loose':
                        success, id = iqoption.buy(BALANCE * 0.02, ACTIVES, 'put', 5)
                        entry_time = time()
                        if success: 
                            status2, profit2 = iqoption.check_win_v3(id)
                            if status2 == 'loose':
                                success, id = iqoption.buy(BALANCE * 0.04, ACTIVES, 'put', 5)
                                entry_time = time()
                                if success: 
                                    status3, profit3 = iqoption.check_win_v3(id)
                                    if status3 == 'loose':
                                        BALANCE = iqoption.get_balance()
                                        print(f"Lose ${profit1 + profit2 + profit3}")
                                        loop = True
                                        continue
                                    else: 
                                        BALANCE = iqoption.get_balance()
                                        print(f"Win ${profit3}")
                                        loop = True
                                        continue
                            else: 
                                BALANCE = iqoption.get_balance()
                                print(f"Win ${profit2}")
                                loop = True
                                continue
                    else: 
                        BALANCE = iqoption.get_balance()
                        print(f"Win ${profit1}")
                        loop = True
                        continue
            else: continue
