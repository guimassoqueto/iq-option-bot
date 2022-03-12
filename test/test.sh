ISTRADING=`cat ISTRADING | head -1`;
if ((ISTRADING==1))
then
	sleep 10;
	./test.sh;
else
	PID=`cat PID`;
	kill -9 $PID;
	echo 0 1> ISTRADING;
fi;
