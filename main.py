#!/usr/bin/python

import sys

file = open(sys.argv[1], "r")
arr = file.read()
file.close

lines = arr.split("\n")
params = lines[0].split(" ")

# Parse First Line
rows = int(params[0])
cols = int(params[1])
vehicules = int(params[2])
rides = int(params[3])
bonus = int(params[4])
simu = int(params[5])

cpt = 0
res = dict()
i = 1
for line in lines:
    if (cpt == vehicules):
        cpt = 0
    res.setdefault(cpt, []).append(i)


