#!/bin/bash

###############################################################################
# Instructions:
################
#
# Implement the body of this script, 
#    following the instructions in instructions/d.rst
#
###############################################################################


year=$1
if [ -d "$year" ]; then
	rm -r "$year"
fi

for i in January February March April May June July August September October November December; do
	mkdir -p "$year"/"$i"
done
exit

