#!/usr/bin/python

import sys

file = open(sys.argv[1], "r")
arr = file.read()
file.close

lines = arr.split("\n")
params = lines[0].split(" ")

row = int(params[0])
column = int(params[1])
vehicle = int(params[2])
ride = int(params[3])
bonus = int(params[4])
steps = int(params[5])

lines.pop(0)

mat = []
res = dict()
i = 0
cpt = 0

for line in lines:
    if ( not line):
        break
    if (cpt == vehicle):
        cpt = 0
    res.setdefault(cpt, []).append(i)
    cpt += 1
    i += 1

file = open(sys.argv[1].split(".")[0] + ".out", "w")
for key, value in res.items():
    string = str("")
    for val in value:
        string += str(val) + " "
    file.write(str(len(value)) + " " + str(string) + "\n")