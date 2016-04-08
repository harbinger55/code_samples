#!/usr/bin/python
import sorters

f = open("./random5000.txt")
list = f.readlines()
f.close()
print "sorting %d lines" % len(list)
sorters.compareSorts(list)
