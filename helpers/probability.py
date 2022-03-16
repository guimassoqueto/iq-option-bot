#! /usr/bin/python3

from time import time
from helping_functions import login_IQ_Option

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
    '15': 0,
    '16': 0,
    '17': 0,
    '18': 0,
    '19': 0,
    '20': 0
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
check, reason = iqoption.connect()
mil = []

ACTIVES = input('Active: ').upper()
RETRIEVED_CANDLES = int(input('Insert a number between 1 and 100: '))

while RETRIEVED_CANDLES < 1 or RETRIEVED_CANDLES > 100:
    RETRIEVED_CANDLES = int(input('Insert a number between 1 and 100: '))

TIMEFRAME = int(input('Insert the timeframe (5, 10, 15, 30, 60, 120 or 300): '))
tf = (5, 10, 15, 30, 60, 120, 300)

while TIMEFRAME not in tf:
    TIMEFRAME = int(input('Insert the timeframe (5, 10, 15, 30, 60, 120 or 300): '))


print(f"Retrieving data from {RETRIEVED_CANDLES * 1000} candles. Please wait...\n")

if check:
    tempo = time()
    for i in range(RETRIEVED_CANDLES):
        x = iqoption.get_candles(ACTIVES, TIMEFRAME, 1000, tempo)
        mil += x
        tempo = int(x[0]['from']) - 1

for candle in mil:
    open_close.append({'open': candle['open'], 'close': candle['close']})

len_open_close = len(open_close)

for candle in open_close:
    consecutive_up(candle['open'], candle['close'])
    consecutive_down(candle['open'], candle['close'])
    stables(candle['open'], candle['close'])

for key, value in CANDLE_SEQ.items():
    print(f"{key} candle(s) sequence: {value}")
