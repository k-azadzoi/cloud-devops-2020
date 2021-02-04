#! /bin/bash
#A script that checks three numbers and outputs a response based on equality criteria.

echo -n "Please enter three numbers (seperated by a space) : "
read x y z

if [[ $x == $y && $y == $z ]] #checks if x is equal to y and y is equal to z
    then
    result="EQUAL";
elif [[ $x == $y || $y == $z || $x == $z ]] #checks if x is equal to y or y is equal to z or x is equal to z
    then
    result="ISOCELES";
else
    result="SCALENE";
fi 

echo "Result : $result"