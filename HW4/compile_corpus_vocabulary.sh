#!/bin/bash

###############################################################################
# Instructions:
###############
#
# Modify this script so that it accepts text from standard input,
#  and prints (to standard output) a list of the unique words present in the input.
#
# Output should be printed with one word per line.
#
# Do not output any lines that consist entirely of whitespace.
#
# Output must be sorted in alphabetical order 
#  (so, for example, the word "any" should be printed before the word "zebra")
#
# HINT: You will likely need to pipe together multiple commands.
#
###############################################################################
sed 's/\ /\
/g' |sort -t ' ' |uniq


# Students - delete this line and put your work here
