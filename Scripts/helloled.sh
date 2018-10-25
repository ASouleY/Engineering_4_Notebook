#!/bin/bash
counter=1
gpio -g mode 17 out
gpio -g mode 19 out
while [ $counter -le 10 ]
do
gpio -g write 17 1
sleep 1
gpio -g write 17 0
gpio -g write 19 1
sleep 1
gpio -g write 19 0
((counter++))
done