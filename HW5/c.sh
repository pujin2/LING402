#!/bin/bash

###############################################################################
# Instructions:
################
#
# Implement the body of this script, 
#    following the instructions in instructions/c.rst
#
###############################################################################


year=$1
if [ -d "$year" ]; then
        rm -r "$year"
fi
mkdir $year
for i in January February March April May June July August September October November December; do
	case $i in
		January)	mkdir $year/$i
 				for n in $(seq 31)
				do
				touch $year/$i/$n
				done
				;;

		February)	mkdir $year/$i
                                for n in $(seq 28)
                                do
                                touch $year/$i/$n
                                done
                                ;;


		March)		mkdir $year/$i
                                for n in $(seq 31)
                                do
                                touch $year/$i/$n
                                done
                                ;;


		April)          mkdir $year/$i
                                for n in $(seq 30)
                                do
                                touch $year/$i/$n
                                done
                                ;;

		May)            mkdir $year/$i
                                for n in $(seq 31)
                                do
                                touch $year/$i/$n
                                done
                                ;;

		June)           mkdir $year/$i
                                for n in $(seq 30)
                                do
                                touch $year/$i/$n
                                done
                                ;;

		July)           mkdir $year/$i
                                for n in $(seq 31)
                                do
                                touch $year/$i/$n
                                done
                                ;;

		August)         mkdir $year/$i
                                for n in $(seq 31)
                                do
                                touch $year/$i/$n
                                done
                                ;;

		September)      mkdir $year/$i
                                for n in $(seq 30)
                                do
                                touch $year/$i/$n
                                done
                                ;;

		October)        mkdir $year/$i
                                for n in $(seq 31)
                                do
                                touch $year/$i/$n
                                done
                                ;;

		November)       mkdir $year/$i
                                for n in $(seq 30)
                                do
                                touch $year/$i/$n
                                done
                                ;;

		December)       mkdir $year/$i
                                for n in $(seq 31)
                                do
                                touch $year/$i/$n
                                done
                                ;;

	esac
done
exit
