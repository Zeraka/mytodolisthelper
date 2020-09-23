#!/bin/bash
filename='todolist.txt'

if [ $# != 0 ] #要隔开
then
sed -i "$1 s/notdone/$2/g " $filename
fi
if [ $# == 0 ]
then
bash showtoday.sh
fi
#echo sed -i "$1 s/notdone/$2/g" $filename