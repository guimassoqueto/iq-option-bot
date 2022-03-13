#! /usr/bin/bash

ISTRADING=`head -n 1 ISTRADING`; 
if (($ISTRADING == 1)); then 
    sleep 8m;
    /home/guilherme/Desktop/iq-option-bot/kill_proccess.sh;
else 
    PID=`head -n 1 PID`;
    kill -9 $PID;
    rm ISTRADING PID;
fi;
