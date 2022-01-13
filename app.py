from multiprocessing import Process
from helping_functions import login_IQ_Option, get_actives_to_trade, generate_processes
from time import sleep, time

def test(iq, active, timeframe, candles_quantity):
    candles = iq.get_candles(active, timeframe, candles_quantity, time())
    current = candles[-1]
    last_candles = candles[:-1]

    with open('test.txt', 'a', encoding='utf-8') as file:
        for candle in last_candles:
            file.write(f"Open: {candle['open']} Close: {candle['close']}\n")

        file.write(f"Open: {current['open']} Close: {current['close']}\n")

ACTIVES = get_actives_to_trade()

if __name__ == "__main__":
    iqoption = login_IQ_Option()
    
    # if connection succeed, connected is True, otherwise False. 
    # error is the details if is the connection fail
    connected, error = iqoption.connect()

    if connected:
        PROCESSES = generate_processes(ACTIVES, test, iqoption)

        for process in PROCESSES.values():
            process.start()
        
        sleep(5)

        for process in PROCESSES.values():
            process.join()