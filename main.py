#! /usr/bin/python3

from time import time, sleep
from helping_functions import login_IQ_Option, consecutive_down, consecutive_up, all_tradeable_actives
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
                balance = BALANCE * 0.0001
                success1, id1 = iqoption.buy(balance, ACTIVE, action, EXPIRATION)

                while not success1:
                    success1, id1 = iqoption.buy(balance, ACTIVE, action, EXPIRATION)

                print('Wait for results (PUT)...')

                status1, profit1 = iqoption.check_win_v3(id1)

                if(status1 == 'loose'):
                    success2, id2 = iqoption.buy(balance * 2.5, ACTIVE, action, EXPIRATION)

                    while not success2:
                        success2, id2 = iqoption.buy(balance * 2.5, ACTIVE, action, EXPIRATION)
                    print('M2')
                    status2, profit2 = iqoption.check_win_v3(id2)

                    if(status2 == 'loose'):
                        success3, id3 = iqoption.buy(balance * 2.5 ** 2, ACTIVE, action, EXPIRATION)

                        while not success3:
                            success3, id3 = iqoption.buy(balance * 2.5 ** 2, ACTIVE, action, EXPIRATION)
                        print('M3')
                        status3, profit3 = iqoption.check_win_v3(id3)

                        if(status3 == 'loose'):
                            success4, id4 = iqoption.buy(balance * 2.5 ** 3, ACTIVE, action, EXPIRATION)

                            while not success4:
                                success4, id4 = iqoption.buy(balance * 2.5 ** 3, ACTIVE, action, EXPIRATION)
                            print('M4')
                            status4, profit4 = iqoption.check_win_v3(id4)

                            if(status4 == 'loose'):
                                success5, id5 = iqoption.buy(balance * 2.5 ** 4, ACTIVE, action, EXPIRATION)

                                while not success5:
                                    success5, id5 = iqoption.buy(balance * 2.5 ** 4, ACTIVE, action, EXPIRATION)
                                print('M5')
                                status5, profit5 = iqoption.check_win_v3(id5)

                                if(status5 == 'loose'):
                                    success6, id6 = iqoption.buy(balance * 2.5 ** 5, ACTIVE, action, EXPIRATION)

                                    while not success6:
                                        success6, id6 = iqoption.buy(balance * 2.5 ** 5, ACTIVE, action, EXPIRATION)
                                    print('M6')
                                    status6, profit6 = iqoption.check_win_v3(id6)

                                    if(status6 == 'loose'):
                                        success7, id7 = iqoption.buy(balance * 2.5 ** 6, ACTIVE, action, EXPIRATION)
                                        print('M7')
                                        while not success7:
                                            success7, id7 = iqoption.buy(balance * 2.5 ** 6, ACTIVE, action, EXPIRATION)
                                        
                                        status7, profit7 = iqoption.check_win_v3(id7)

                                        if (status7 == 'loose'):
                                            print(f"You lose ${profit1 + profit2 + profit3 + profit4 + profit5 + profit6 + profit7}")
                                            BALANCE = iqoption.get_balance()
                                            loop = True
                                        elif(status7 == 'win'):
                                            print(f"You win ${profit7 + profit6 + profit5 + profit4 + profit3 + profit2 + profit1}")
                                            BALANCE = iqoption.get_balance()
                                            loop = True
                                        else:
                                            print(f"DRAW")
                                            sleep(600)
                                            BALANCE = iqoption.get_balance()
                                            loop = True
                                    elif(status6 == 'win'):
                                        print(f"You win ${profit6 + profit5 + profit4 + profit3 + profit2 + profit1}")
                                        BALANCE = iqoption.get_balance()
                                        loop = True
                                    else:
                                        print(f"DRAW")
                                        sleep(600)
                                        BALANCE = iqoption.get_balance()
                                        loop = True
                                elif(status5 == 'win'):
                                    print(f"You win ${profit5 + profit4 + profit3 + profit2 + profit1}")
                                    BALANCE = iqoption.get_balance()
                                    loop = True
                                else:
                                    print(f"DRAW")
                                    sleep(600)
                                    BALANCE = iqoption.get_balance()
                                    loop = True
                            elif(status4 == 'win'):
                                print(f"You win ${profit4 + profit3 + profit2 + profit1}")
                                BALANCE = iqoption.get_balance()
                                loop = True
                            else:
                                print(f"DRAW")
                                sleep(600)
                                BALANCE = iqoption.get_balance()
                                loop = True
                        elif(status3 == 'win'):
                            print(f"You win ${profit3 + profit2 + profit1}")
                            BALANCE = iqoption.get_balance()
                            loop = True
                        else:
                            print(f"DRAW")
                            sleep(600)
                            BALANCE = iqoption.get_balance()
                            loop = True
                    elif(status2 == 'win'):
                        print(f"You win ${profit2 + profit1}")
                        BALANCE = iqoption.get_balance()
                        loop = True
                    else:
                        print(f"DRAW")
                        sleep(600)
                        BALANCE = iqoption.get_balance()
                        loop = True
                elif(status1 == 'win'):
                    print(f"You win ${profit1}")
                    BALANCE = iqoption.get_balance()
                    loop = True
                else:
                    print(f"DRAW")
                    sleep(600)
                    BALANCE = iqoption.get_balance()
                    loop = True
                                            
            if consecutive_down(last_candles):
                loop = False
                action = 'call'
                balance = BALANCE * 0.0001
                success1, id1 = iqoption.buy(balance, ACTIVE, action, EXPIRATION)

                while not success1:
                    success1, id1 = iqoption.buy(balance, ACTIVE, action, EXPIRATION)

                print("Wait for results (CALL)...")

                status1, profit1 = iqoption.check_win_v3(id1)

                if(status1 == 'loose'):
                    success2, id2 = iqoption.buy(balance * 2.5, ACTIVE, action, EXPIRATION)

                    while not success2:
                        success2, id2 = iqoption.buy(balance * 2.5, ACTIVE, action, EXPIRATION)
                    print('M2')
                    status2, profit2 = iqoption.check_win_v3(id2)

                    if(status2 == 'loose'):
                        success3, id3 = iqoption.buy(balance * 2.5 ** 2, ACTIVE, action, EXPIRATION)

                        while not success3:
                            success3, id3 = iqoption.buy(balance * 2.5 ** 2, ACTIVE, action, EXPIRATION)
                        print('M3')
                        status3, profit3 = iqoption.check_win_v3(id3)

                        if(status3 == 'loose'):
                            success4, id4 = iqoption.buy(balance * 2.5 ** 3, ACTIVE, action, EXPIRATION)

                            while not success4:
                                success4, id4 = iqoption.buy(balance * 2.5 ** 3, ACTIVE, action, EXPIRATION)
                            print('M4')
                            status4, profit4 = iqoption.check_win_v3(id4)

                            if(status4 == 'loose'):
                                success5, id5 = iqoption.buy(balance * 2.5 ** 4, ACTIVE, action, EXPIRATION)

                                while not success5:
                                    success5, id5 = iqoption.buy(balance * 2.5 ** 4, ACTIVE, action, EXPIRATION)
                                print('M5')
                                status5, profit5 = iqoption.check_win_v3(id5)

                                if(status5 == 'loose'):
                                    success6, id6 = iqoption.buy(balance * 2.5 ** 5, ACTIVE, action, EXPIRATION)

                                    while not success6:
                                        success6, id6 = iqoption.buy(balance * 2.5 ** 5, ACTIVE, action, EXPIRATION)
                                    print('M6')
                                    status6, profit6 = iqoption.check_win_v3(id6)

                                    if(status6 == 'loose'):
                                        success7, id7 = iqoption.buy(balance * 2.5 ** 6, ACTIVE, action, EXPIRATION)

                                        while not success7:
                                            success7, id7 = iqoption.buy(balance * 2.5 ** 6, ACTIVE, action, EXPIRATION)
                                        print('M7')
                                        status7, profit7 = iqoption.check_win_v3(id7)

                                        if (status7 == 'loose'):
                                            print(f"You lose ${profit1 + profit2 + profit3 + profit4 + profit5 + profit6 + profit7}")
                                            BALANCE = iqoption.get_balance()
                                            loop = True
                                        elif(status7 == 'win'):
                                            print(f"You win ${profit7 + profit6 + profit5 + profit4 + profit3 + profit2 + profit1}")
                                            BALANCE = iqoption.get_balance()
                                            loop = True
                                        else:
                                            print(f"DRAW")
                                            sleep(300)
                                            BALANCE = iqoption.get_balance()
                                            loop = True
                                    elif(status6 == 'win'):
                                        print(f"You win ${profit6 + profit5 + profit4 + profit3 + profit2 + profit1}")
                                        BALANCE = iqoption.get_balance()
                                        loop = True
                                    else:
                                        print(f"DRAW")
                                        sleep(300)
                                        BALANCE = iqoption.get_balance()
                                        loop = True
                                elif(status5 == 'win'):
                                    print(f"You win ${profit5 + profit4 + profit3 + profit2 + profit1}")
                                    BALANCE = iqoption.get_balance()
                                    loop = True
                                else:
                                    print(f"DRAW")
                                    sleep(300)
                                    BALANCE = iqoption.get_balance()
                                    loop = True
                            elif(status4 == 'win'):
                                print(f"You win ${profit4 + profit3 + profit2 + profit1}")
                                BALANCE = iqoption.get_balance()
                                loop = True
                            else:
                                print(f"DRAW")
                                sleep(300)
                                BALANCE = iqoption.get_balance()
                                loop = True
                        elif(status3 == 'win'):
                            print(f"You win ${profit3 + profit2 + profit1}")
                            BALANCE = iqoption.get_balance()
                            loop = True
                        else:
                            print(f"DRAW")
                            sleep(300)
                            BALANCE = iqoption.get_balance()
                            loop = True
                    elif(status2 == 'win'):
                        print(f"You win ${profit2 + profit1}")
                        BALANCE = iqoption.get_balance()
                        loop = True
                    else:
                        print(f"DRAW")
                        sleep(300)
                        BALANCE = iqoption.get_balance()
                        loop = True
                elif(status1 == 'win'):
                    print(f"You win ${profit1}")
                    BALANCE = iqoption.get_balance()
                    loop = True
                else:
                    print(f"DRAW")
                    sleep(300)
                    BALANCE = iqoption.get_balance()
                    loop = True
