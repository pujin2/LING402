#!/bin/bash

###############################################################################
# Instructions:
###############
#
# Modify this script so that it transforms the contents of the file /etc/password
#  into a list of usernames (one username per line), sorted alphabetically,
#  printing the output to standard output.
#
###############################################################################

cut -d ':' -f 1 /etc/passwd | sort 

