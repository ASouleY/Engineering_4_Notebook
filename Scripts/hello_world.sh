#!/bin/bash
counter=1
str="Hello World!"
while [ $counter -le 10 ]
do
echo $str
((counter++))
done

