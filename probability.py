#! /usr/bin/python3

from time import time
from helpers import login_IQ_Option

arr = []
UP = 0
DOWN = 0
CANDLE_SEQ = {
    'stable': 0,
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0,
    '10': 0,
    '11': 0,
    '12': 0,
    '13': 0,
    '14': 0,
    '15': 0
}
open_close = []

def consecutive_up(candle_open: float, candle_close: float) -> None:
    global UP
    if candle_open < candle_close: 
        UP += 1
        CANDLE_SEQ[str(UP)] += 1
    else: UP = 0

def consecutive_down(candle_open: float, candle_close: float) -> None:
    global DOWN
    if candle_open > candle_close: 
        DOWN += 1
        CANDLE_SEQ[str(DOWN)] += 1
    else: DOWN = 0

def stables(candle_open: float, candle_close: float) -> None:
    if candle_open == candle_close: CANDLE_SEQ['stable'] += 1
        
iqoption = login_IQ_Option()
check,reason = iqoption.connect()
ACTIVES = input('Pair: ').upper()

if check:
    mil = iqoption.get_candles(ACTIVES, 60, 1000, time())

for candle in mil:
    open_close.append({'open': candle['open'], 'close': candle['close']})

len_open_close = len(open_close)

for candle in open_close:
    consecutive_up(candle['open'], candle['close'])
    consecutive_down(candle['open'], candle['close'])
    stables(candle['open'], candle['close'])

for key, value in CANDLE_SEQ.items():
    print(f"{key} candle(s) sequence: {value}")