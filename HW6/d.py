#!/usr/bin/python3
from nltk.corpus import udhr
count=0
for file in udhr.fileids():
        count=count+1
        print("{:03} {}".format(count,file))

