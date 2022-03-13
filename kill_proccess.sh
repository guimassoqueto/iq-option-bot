#! /usr/bin/bash

ISTRADING=`head -n 1 ISTRADING`; 
if (($ISTRADING == 1)); then 
    sleep 8m;
    ./kill_process.sh;
else 
    PID=`head -n 1 PID`;
    kill -9 $PID;
    rm ISTRADING PID;
fi;