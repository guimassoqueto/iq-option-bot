#! /usr/bin/python3
from csv import DictWriter
from iqoptionapi.stable_api import IQ_Option
from os import environ
import threading

def login_IQ_Option():
    return IQ_Option(environ['MY_EMAIL'], environ['IQ_OPTION_PWD'])

def consecutive_down(last_six: list) -> bool:
    [c5, c4, c3, c2, c1, c0] = last_six
    return c5['close'] > c4['close'] and c4['close'] > c3['close'] and c3['close'] > c2['close'] and c2['close'] > c1['close'] and c1['close'] > c0['open']

def consecutive_up(last_six: list) -> bool:
    [c5, c4, c3, c2, c1, c0] = last_six
    return c5['close'] < c4['close'] and c4['close'] < c3['close'] and c3['close'] < c2['close'] and c2['close'] < c1['close'] and c1['close'] < c0['open']

def write_operation_csv(operation: dict) -> None:
    with open('operacoes_iqoption.csv', 'a', newline='') as csvfile:
        fieldnames = ['active','entry_time', 'entry_money', 'exit_time','profit_loss']
        writer = DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(operation)

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t