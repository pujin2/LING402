#!/bin/bash

###############################################################################
# Instructions:
###############
#
# Modify this script so that it takes text from standard input
#  performs spell check, and prints a list of misspelled words (one word per line)
#  to standard output
#
##############################################################################
aspell list | sed 's/\ /\
/g' 

# Students - delete this line and put your work here
