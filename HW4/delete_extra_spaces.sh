#!/bin/bash

###############################################################################
# Instructions:
###############
#
# Modify this script so that it accepts text from standard input,
#  performing a "squeeze" operation on any repeated adjacent instances of the space character,
#  printing the result to standard output
#
# In other words, "This    is an   example   of text     with too many    extra   spaces.  "
#  should be converted to "This is an example of text with too many extra spaces. "
#
# HINT: The solution to this problem is discussed in Chapter 20 of the assigned reading
#
###############################################################################
tr -s '/ '


# Students - delete this line and put your work here
