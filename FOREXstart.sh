#!/bin/bash

ACTIVES=('eurusd' 'eurjpy' 'eurgbp')

# Our custom function
cust_func(){
  /home/guilherme/Desktop/iq-option-bot/main_2seq.py $1 60 
}

# For loop 5 times
for i in ${ACTIVES[@]};
do
	cust_func $i & # Put a function in the background
done
 
## Put all cust_func in the background and bash 
## would wait until those are completed 
## before displaying all done message
wait 
echo "All done"
