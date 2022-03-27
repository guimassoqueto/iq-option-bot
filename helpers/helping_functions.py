#! /usr/bin/python3

from sys import argv
from csv import writer
from iqoptionapi.stable_api import IQ_Option
from os import environ, getpid, getcwd
from os.path import abspath, join
import threading
from datetime import datetime
from multiprocessing import Process
from iqoptionapi.constants import ACTIVES
from time import sleep

expiration_mode = {
    '30': .5,
    '60': 1,
    '120': 2,
    '300': 5
}

def login_IQ_Option():
    return IQ_Option(environ['MY_EMAIL'], environ['IQ_OPTION_PWD'])


def select_active_timeframe_v1() -> None:
    '''
    Select and return ACTIVE, TIMEFRAME and EXPIRATION
    '''
    all_act = all_tradeable_actives()

    ACTIVE = input('Active: ').upper()
    while ACTIVE not in all_act:
        ACTIVE = input('Active: ').upper()

    TIMEFRAME = int(input('Timeframe (30, 60, 120 or 300): '))
    while TIMEFRAME not in (30, 60, 120, 300):
        TIMEFRAME = int(input('Timeframe (30, 60, 120 or 300): '))

    return (ACTIVE, TIMEFRAME, expiration_mode[str(TIMEFRAME)])


def select_active_timeframe_v2() -> tuple:
    '''
    Select and return ACTIVE, TIMEFRAME and EXPIRATION based on terminal args
    '''
    if len(argv) == 3:
        ACTIVE = argv[1].upper()
        TIMEFRAME = int(argv[2])
        if (ACTIVE not in all_tradeable_actives()) or (TIMEFRAME not in (30, 60, 120, 300)):
            raise Exception(f"{ACTIVE} isn't a valid active or {TIMEFRAME} isn't a valid timeframe.")
    else:
        raise Exception("There isn't enough args.")
    
    return (ACTIVE, TIMEFRAME, expiration_mode[str(TIMEFRAME)])


def select_active_timeframe_candlecount() -> tuple:
    '''
    Select and return ACTIVE, TIMEFRAME and CANDLES RETRIEVED based on terminal args
    '''
    if len(argv) == 4:
        ACTIVE = argv[1].upper()
        TIMEFRAME = int(argv[2])
        RETRIEVED_CANDLES = int(argv[3])
        if (ACTIVE not in all_tradeable_actives()) or (TIMEFRAME not in (30, 60, 120, 300) or (RETRIEVED_CANDLES < 1 or RETRIEVED_CANDLES > 100)):
            raise Exception(f"{ACTIVE} isn't a valid active or {TIMEFRAME} isn't a valid timeframe.")
    else:
        raise Exception("There isn't enough args.")
    
    return (ACTIVE, TIMEFRAME, RETRIEVED_CANDLES)


def consecutive_up(last_five: list) -> bool:
    [c5, c4, c3, c2, c1] = last_five
    return c5['open'] < c5['close'] and c4['open'] < c4['close'] and c3['open'] < c3['close'] and c2['open'] < c2['close'] and c1['open'] < c1['close']


def consecutive_down(last_five: list) -> bool:
    [c5, c4, c3, c2, c1] = last_five
    return c5['open'] > c5['close'] and c4['open'] > c4['close'] and c3['open'] > c3['close'] and c2['open'] > c2['close'] and c1['open'] > c1['close']


def write_consecutives(active: str, up_or_down: str) -> None:
    now = datetime.now().strftime("%d/%m/%y %H:%M:%S")
    with open('consecutive_candles.csv', 'a', encoding='utf-8', newline='') as csvfile:
        spamwriter = writer(csvfile)
        spamwriter.writerow([active, up_or_down, now])


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


def all_tradeable_actives() -> list:
    '''Return a list of IQ Options' actives able to trade'''
    return [active for active in ACTIVES.keys()]


def get_actives_to_trade() -> list:
    '''
    Get user's actives that he want to trade. 1 for CPU.
    '''
    all_actives = all_tradeable_actives()
    loop = True
    actives = []
    count = 1 # cpu_count()

    while loop:
        active = input(f"Active ({count} left): ").upper()
        
        if active not in all_actives: 
            active = input(f"Active ({count} left): ").upper()
        else:
            if active not in actives:
                actives.append(active)
                count -= 1
            else: continue
        
        if count == 0: loop = False
        
    return actives


def get_timeframe_to_trade() -> int:
    '''
        Creates the timeframe based on user' timeframe selection
    '''
    timeframe = input('Timeframe (30, 60, 120, 300): ')

    while timeframe not in ('30', '60', '120', '300'):
        timeframe = input('Timeframe (30, 60, 120, 300): ')

    return int(timeframe)


def generate_processes(actives_list: list, func, iq: object) -> dict:
    '''
    Generates an process dictionary of all the user's chosen actives
    '''
    timeframe = get_timeframe_to_trade()

    processes = {}

    for active in actives_list:
        processes[active] = Process(target=func, args=(iq, active, timeframe, 6))

    return processes


def enter_operation(iq: object, active: str, action: str, balance: float, multiplier: int, expiration: int) -> tuple:
    '''
    Start an operation
    '''
    gale = 1
    if multiplier: 
        gale = 2.5 ** multiplier
        print(f"M{multiplier + 1}")

    price = balance * 0.0001 * gale

    success, id = iq.buy(price, active, action, expiration)

    while not success:
        success, id = iq.buy(price, active, action, expiration)

    write_is_trading(active, 1)
    print(f"{active} - Wait for results ({action.upper()})...")

    return iq.check_win_v4(id)


def trade_result(iq: object, profit: float, active: str)-> tuple:
    '''
    Print to the user the result of an operation, update the balance and continue the loop
    '''
    if profit < 0:
        print(f"You lose ${profit}")
    else:
        print(f"You won ${profit}")

    write_is_trading(active, 0)
    sleep(360)

    return (True, iq.get_balance())


def write_process(active: str) -> None:
    '''
    Write the process number in the file PID
    '''
    f = open(f'/home/guilherme/Desktop/iq-option-bot/trades/pid/{active}', 'w', encoding='utf-8')
    f.write(f"{getpid()}")
    f.close()


def write_is_trading(active:str, istrading: int) -> None:
    '''
    Write and return if the program is trading at the given moment (0: false, 1: true)
    '''
    f = open(f'/home/guilherme/Desktop/iq-option-bot/trades/istrading/{active}', 'w', encoding='utf-8')
    f.write(f"{istrading}")
    f.close()
