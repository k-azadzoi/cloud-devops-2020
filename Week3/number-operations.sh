#! /bin/bash
#A script that will take two numbers then add, subtract, multiply, and divide the two.

read x
read y

add=$(( x + y ))
sub=$(( x - y ))
mul=$(( x * y ))
div=$(( x / y ))

echo "$add"
echo "$sub"
echo "$mul"
echo "$div"