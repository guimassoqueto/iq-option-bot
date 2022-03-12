#! /usr/bin/python3
from os import getpid
from random import randint
from time import sleep

def write_process() -> None:
    '''
    Write the process number in the file PID
    '''
    f = open('PID', 'w', encoding='utf-8')
    f.write(f"{getpid()}")
    f.close()

def write_is_trading() -> None:
    
is_trading = randint(0,1)

if is_trading:
    f = open('ISTRADING', 'w', encoding='utf-8')
    f.write("1")
    f.close()

    while True:
        print('Ok')
        sleep(5)
else:
    f = open('ISTRADING', 'w', encoding='utf-8')
    f.write("0")
    f.close()
