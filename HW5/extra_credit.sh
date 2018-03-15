#!/bin/bash

###############################################################################
# Instructions:
################
#
# Implement the body of this script, 
#    following the instructions in instructions/extra_credit.rst
#
###############################################################################

number=$#
if [ $number -eq 1 ]; then
        year=$1
        number=$1
        digit=0
        while [ $number -gt 0 ]
        do
                number=$(($number / 10))
                digit=$(( $digit +1 ))
        done
        if [ $digit -eq 4 ]; then

                if [ -d "$year" ]; then
                rm -r "$year"
                fi
                mkdir $year
		for (( i=1; i<=12; i=i+1 )); do
			mkdir $year/$(date -d "$i/1" "+%B")
			for d in $(ncal -b "$i" "$year" | tail -n +3); do
       				 wget -q -O $year/$(date -d "$i/1" "+%B")/"$d".html https://en.wikipedia.org/w/index.php?title="$(date -d "$i/1" "+%B")"_"$d"&printable=yes 
			done
		done
        else
                echo "Usage: $0 year"
        fi
else
        echo "Usage: $0 year"
fi
exit

