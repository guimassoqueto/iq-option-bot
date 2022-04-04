#! /usr/bin/python3

from time import time, sleep
from helpers.helping_functions import (
    login_IQ_Option,
    select_active_timeframe_v2,
    consecutive_down, 
    consecutive_up, 
    enter_operation, 
    trade_result,
    set_interval,
    write_process,
    write_is_trading
)

ACTIVE, TIMEFRAME, EXPIRATION = select_active_timeframe_v2()

write_process(ACTIVE)
write_is_trading(ACTIVE, 0)

iqoption = login_IQ_Option()
CHECK, _ = iqoption.connect()
# iqoption.change_balance("REAL")
BALANCE = iqoption.get_balance()

PAYOUT = iqoption.
# ######################################################
# def check_conn() -> None:
#     '''
#     função que checa status da conexão
#     '''
#     conn = iqoption.check_connect()
#     if not conn:
#         CHECK, _ = iqoption.connect()

#         while not CHECK:
#             print('Trying to reconnect...')
#             CHECK, _ = iqoption.connect()
            
#         print('Reconnected!')

# set_interval(check_conn, 15)
# ########################################################

# if CHECK:
#     loop = True
#     arr = [0,0]
#     while loop:
#         candles = iqoption.get_candles(ACTIVE, TIMEFRAME, 6, time())
#         current = candles[-1]
#         last_candles = candles[:-1]

#         if current['to'] not in arr:
#             arr.append(current['to'])
#             arr = arr[1:]

#             if consecutive_up(last_candles):
#                 loop = False
#                 action = 'put'
#                 status0, p0 = enter_operation(iqoption, ACTIVE, action, BALANCE, 0, EXPIRATION)

#                 if(status0 == 'loose'):
#                     status1, p1 = enter_operation(iqoption, ACTIVE, action, BALANCE, 1, EXPIRATION)

#                     if(status1 == 'loose'):
#                         status2, p2 = enter_operation(iqoption, ACTIVE, action, BALANCE, 2, EXPIRATION)

#                         if(status2 == 'loose'):
#                             status3, p3 = enter_operation(iqoption, ACTIVE, action, BALANCE, 3, EXPIRATION)

#                             if(status3 == 'loose'):
#                                 status4, p4 = enter_operation(iqoption, ACTIVE, action, BALANCE, 4, EXPIRATION)

#                                 if(status4 == 'loose'):
#                                     status5, p5 = enter_operation(iqoption, ACTIVE, action, BALANCE, 5, EXPIRATION)

#                                     if(status5 == 'loose'):
#                                         status6, p6 = enter_operation(iqoption, ACTIVE, action, BALANCE, 6, EXPIRATION)

#                                         if (status6 == 'loose'):
#                                             sleep(600)
#                                             loop, BALANCE = trade_result(iqoption, p6 + p5 + p4 + p3 + p2 + p1 + p0, ACTIVE)                                            
#                                         else:
#                                             loop, BALANCE = trade_result(iqoption, p6 + p5 + p4 + p3 + p2 + p1 + p0, ACTIVE)                                    
#                                     else:
#                                         loop, BALANCE = trade_result(iqoption, p5 + p4 + p3 + p2 + p1 + p0, ACTIVE)
#                                 else:
#                                     loop, BALANCE = trade_result(iqoption, p4 + p3 + p2 + p1 + p0, ACTIVE)
#                             else:
#                                 loop, BALANCE = trade_result(iqoption, p3 + p2 + p1 + p0, ACTIVE)
#                         else:
#                             loop, BALANCE = trade_result(iqoption, p2 + p1 + p0, ACTIVE)
#                     else:
#                         loop, BALANCE = trade_result(iqoption, p1 + p0, ACTIVE)
#                 else:
#                     loop, BALANCE = trade_result(iqoption, p0, ACTIVE)

#             if consecutive_down(last_candles):
#                 loop = False
#                 action = 'call'
#                 status0, p0 = enter_operation(iqoption, ACTIVE, action, BALANCE, 0, EXPIRATION)

#                 if(status0 == 'loose'):
#                     status1, p1 = enter_operation(iqoption, ACTIVE, action, BALANCE, 1, EXPIRATION)

#                     if(status1 == 'loose'):
#                         status2, p2 = enter_operation(iqoption, ACTIVE, action, BALANCE, 2, EXPIRATION)

#                         if(status2 == 'loose'):
#                             status3, p3 = enter_operation(iqoption, ACTIVE, action, BALANCE, 3, EXPIRATION)

#                             if(status3 == 'loose'):
#                                 status4, p4 = enter_operation(iqoption, ACTIVE, action, BALANCE, 4, EXPIRATION)

#                                 if(status4 == 'loose'):
#                                     status5, p5 = enter_operation(iqoption, ACTIVE, action, BALANCE, 5, EXPIRATION)

#                                     if(status5 == 'loose'):
#                                         status6, p6 = enter_operation(iqoption, ACTIVE, action, BALANCE, 6, EXPIRATION)

#                                         if (status6 == 'loose'):
#                                             loop, BALANCE = trade_result(iqoption, p6 + p5 + p4 + p3 + p2 + p1 + p0, ACTIVE)
#                                         else:
#                                             loop, BALANCE = trade_result(iqoption, p6 + p5 + p4 + p3 + p2 + p1 + p0, ACTIVE)
#                                     else:
#                                         loop, BALANCE = trade_result(iqoption, p5 + p4 + p3 + p2 + p1 + p0, ACTIVE)
#                                 else:
#                                     loop, BALANCE = trade_result(iqoption, p4 + p3 + p2 + p1 + p0, ACTIVE)
#                             else:
#                                 loop, BALANCE = trade_result(iqoption, p3 + p2 + p1 + p0, ACTIVE)
#                         else:
#                             loop, BALANCE = trade_result(iqoption, p2 + p1 + p0, ACTIVE)
#                     else:
#                         loop, BALANCE = trade_result(iqoption, p1 + p0, ACTIVE)
#                 else:
#                     loop, BALANCE = trade_result(iqoption, p0, ACTIVE)
#         else: continue
        
