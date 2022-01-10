#! /usr/bin/python3

from csv import writer
from iqoptionapi.stable_api import IQ_Option
from os import environ
import threading
from datetime import datetime

def login_IQ_Option():
    return IQ_Option(environ['MY_EMAIL'], environ['IQ_OPTION_PWD'])

def consecutive_up(last_five: list) -> bool:
    [c5, c4, c3, c2, c1] = last_five
    return c5['open'] < c5['close'] and c4['open'] < c4['close'] and c3['open'] < c3['close'] and c2['open'] < c2['close'] and c1['open'] < c1['close']

def consecutive_down(last_five: list) -> bool:
    [c5, c4, c3, c2, c1] = last_five
    return c5['open'] > c5['close'] and c4['open'] > c4['close'] and c3['open'] > c3['close'] and c2['open'] > c2['close'] and c1['open'] > c1['close']

def write_delay(active: str, timeframe: int, action: str, delay: float) -> None:
    with open('entry_delays.csv', 'a', encoding='utf-8', newline='') as csvfile:
        spamwriter = writer(csvfile)
        spamwriter.writerow([active, timeframe, action, delay])

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