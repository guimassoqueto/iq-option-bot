#! /usr/bin/python3

from time import time, sleep
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
                success1, id1 = iqoption.buy(BALANCE * 0.01, ACTIVES, 'call', 5)

                while not success1:
                    success1, id1 = iqoption.buy(BALANCE * 0.01, ACTIVES, 'call', 5)
                
                status1, profit1 = iqoption.check_win_v3(id1)

                if status1 == 'loose':
                    success2, id2 = iqoption.buy(BALANCE * 0.01, ACTIVES, 'call', 5)

                    while not success2:
                        success2, id2 = iqoption.buy(BALANCE * 0.01, ACTIVES, 'call', 5)
                    
                    status2, profit2 = iqoption.check_win_v3(id2)
                    
                    if status2 == 'loose':
                        success3, id3 = iqoption.buy(BALANCE * 0.01, ACTIVES, 'call', 5)

                        while not success3:
                            success3, id3 = iqoption.buy(BALANCE * 0.01, ACTIVES, 'call', 5)

                        status3, profit3 = iqoption.check_win_v3(id2)
                    
                        if status3 == 'loose':
                            print(f"You lose {profit1, profit2, profit3}")
                            BALANCE = iqoption.get_balance()
                            sleep(1800)
                            loop = True
                        else: 
                            print(f"You win {profit3}")
                            BALANCE = iqoption.get_balance()
                            sleep(1800)
                            loop = True
                    else: 
                        print(f"You win {profit2}")
                        BALANCE = iqoption.get_balance()
                        sleep(1800)
                        loop = True
                else: 
                    print(f"You win {profit1}")
                    BALANCE = iqoption.get_balance()
                    sleep(1800)
                    loop = True

            if consecutive_up(last_six):
                loop = False              
                success1, id1 = iqoption.buy(BALANCE * 0.01, ACTIVES, 'put', 5)

                while not success1:
                    success1, id1 = iqoption.buy(BALANCE * 0.01, ACTIVES, 'put', 5)
                
                status1, profit1 = iqoption.check_win_v3(id1)

                if status1 == 'loose':
                    success2, id2 = iqoption.buy(BALANCE * 0.01, ACTIVES, 'put', 5)

                    while not success2:
                        success2, id2 = iqoption.buy(BALANCE * 0.01, ACTIVES, 'put', 5)
                    
                    status2, profit2 = iqoption.check_win_v3(id2)
                    
                    if status2 == 'loose':
                        success3, id3 = iqoption.buy(BALANCE * 0.01, ACTIVES, 'put', 5)

                        while not success3:
                            success3, id3 = iqoption.buy(BALANCE * 0.01, ACTIVES, 'put', 5)

                        status3, profit3 = iqoption.check_win_v3(id2)
                    
                        if status3 == 'loose':
                            print(f"You lose {profit1, profit2, profit3}")
                            BALANCE = iqoption.get_balance()
                            sleep(1800)
                            loop = True
                        else: 
                            print(f"You win {profit3}")
                            BALANCE = iqoption.get_balance()
                            sleep(1800)
                            loop = True
                    else: 
                        print(f"You win {profit2}")
                        BALANCE = iqoption.get_balance()
                        sleep(1800)
                        loop = True
                else: 
                    print(f"You win {profit1}")
                    BALANCE = iqoption.get_balance()
                    sleep(1800)
                    loop = True
            else: continue
