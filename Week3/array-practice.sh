#!/bin/bash

#creating a new array
arr=("ken" "joe" "dan")

#adding to the array
arr+=("brandon" "francis")

#print out how many elements in the array using ${arr[@]}
echo "the array contains ${#arr[@]} elements" #the array contains 5 elements
c
#print out all the elements in the array
echo ${arr[@]} #prints out ken joe dan brandon francis