#! /usr/bin/bash

PIDS='/home/guilherme/Desktop/trades/pid';
ISTRADINGS='/home/guilherme/Desktop/trades/istrading';

for f in `ls $ISTRADINGS`; 
do
	ISTRADING=`head -1 $ISTRADINGS/$f`;

	if (($ISTRADING == 0))
	then
		pid=`head -1 $PIDS/$f`;
		kill -9 $pid;

		rm $PIDS/$f;
		rm $ISTRADINGS/$f;
	else
		sleep 5;
		/home/guilherme/Desktop/iq-option-bot/kill.sh;
	fi
done
