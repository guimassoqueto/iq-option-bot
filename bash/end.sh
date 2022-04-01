#! /usr/bin/bash

PIDS='/home/guilherme/Desktop/iq-option-bot/trades/pid';
ISTRADINGS='/home/guilherme/Desktop/iq-option-bot/trades/istrading';

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
		sleep 60;
		/home/guilherme/Desktop/iq-option-bot/bash/end.sh;
	fi
done
