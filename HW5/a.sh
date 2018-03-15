#!/bin/bash

###############################################################################
# Instructions:
################
#
# Implement the body of this script, 
#    following the instructions in instructions/a.rst
#
###############################################################################

number=$#
if [ $number -eq 1 ]; then
	year=$1
	if [[ "$year" =~ ^[0-9][0-9][0-9][0-9]$ ]]; then
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
                                	wget -q -O $year/$i/"$n".html https://en.wikipedia.org/w/index.php?title="$i"_"$n"&printable=yes
                                	done
                                	;;

                	February)       if [ $((year%400)) -eq 0 ]; then
                                        	mkdir $year/$i
                                        	for n in $(seq 29)
                                        	do
						wget -q -O $year/$i/"$n".html https://en.wikipedia.org/w/index.php?title="$i"_"$n"&printable=yes
                                        	done
                                	elif [ $((year%100)) -eq 0 ]; then
                                        	mkdir $year/$i
                                        	for n in $(seq 28)
                                        	do
                                        	wget -q -O $year/$i/"$n".html https://en.wikipedia.org/w/index.php?title="$i"_"$n"&printable=yes
                                        	done
					elif [ $((year%4)) -eq 0 ]; then
						mkdir $year/$i
                                                for n in $(seq 29)
                                                do
                                                wget -q -O $year/$i/"$n".html https://en.wikipedia.org/w/index.php?title="$i"_"$n"&printable=yes
                                                done
					else					
                                                mkdir $year/$i
                                                for n in $(seq 28)
                                                do
                                                wget -q -O $year/$i/"$n".html https://en.wikipedia.org/w/index.php?title="$i"_"$n"&printable=yes
                                                done
                                	fi
                                	;;

                	April|June|September|November)
                                	mkdir $year/$i
                                	for n in $(seq 30)
                                	do
                                	wget -q -O $year/$i/"$n".html https://en.wikipedia.org/w/index.php?title="$i"_"$n"&printable=yes
                                	done
                                	;;
                	esac
        	done
	else
		echo "Usage: $0 year"
	fi
else
        echo "Usage: $0 year"
fi
exit
