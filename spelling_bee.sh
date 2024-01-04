#!/bin/bash
if [ "$1" == "" ]; then
   echo "Enter search letters (all upper case): "
   read line
else
   line=$1
fi

egrep "^[$line]{4}[$line]*$" words.txt | grep "P"
