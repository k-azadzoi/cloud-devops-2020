#! /bin/bash
#A script that takes in a reasponse, checks if yY or nN then outputs appropriate response

read response 

if [[ $response == "y" || $response == "Y" ]] #checks if the response is y or Y
    then
    echo "YES"
elif [[ $response == "n" || $response == "N" ]]#checks if the response is n or N
    then
    echo "NO"
else 
    echo "Please enter y or n" #if not either yY or Nn then output
fi