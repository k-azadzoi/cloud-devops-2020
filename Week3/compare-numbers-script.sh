#! /bin/bash
#A simple script that will two numbers and compare them.

read x 
read y

if [ "$x" -gt "$y" ] #checks if x is greater than y then output a message 
    then
    echo "X is greater than Y"
elif [ "$x" -lt "$y" ] #checks if x is less than y then output a message
    then    
    echo "X is less than Y"
elif [ "$x" -eq "$y" ] #checks if x equal to y then output a message
    then
    echo "X is equal to Y"
fi