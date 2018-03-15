#!/bin/bash

###############################################################################
# Instructions:
################
#
# Implement the body of this script, 
#    following the instructions in instructions/b.rst
#
###############################################################################
number=$#
if [ $number -eq 1 ]; then
	
	year=$1
	if [ -d "$year" ]; then
        rm -r "$year"
	fi
	mkdir $year
	for i in January February March April May June July August September October November December; do
        case $i in
                January|March|May|July|August|October|December)        
				mkdir $year/$i
                                for n in $(seq 31)
                                do
                                touch $year/$i/$n
                                done
                                ;;

                February)       if [ $((year%4)) -eq 0 ]; then
					mkdir $year/$i
                                	for n in $(seq 29)
                                	do
                                	touch $year/$i/$n
                                	done
				else
                                        mkdir $year/$i
                                        for n in $(seq 28)
                                        do
                                        touch $year/$i/$n
                                        done
				fi
                                ;;

           	April|June|September|November)
                                mkdir $year/$i
                                for n in $(seq 30)
                                do
                                touch $year/$i/$n
                                done
                                ;;
		esac
	done
else
	echo "Usage: $0 year"
fi
	exit

