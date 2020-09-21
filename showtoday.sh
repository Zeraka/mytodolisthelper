#!/bin/sh
list='todolist.txt'

dt=`date "+ %Y-%m-%d"`;
grep $dt $list;