#!/usr/bin/python

import sys

class Point:
    def __init__(self,x , y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
class Triplet:
    def __init__(self, ride, distance):
        self.ride = ride
        self.distance = distance
        self.marked = False
class Ride:
    def __init__(self, id, d, a, step):
        self.id = id
        self.d = d
        self.a = a
        self.step = step
    def getDepart(self):
        return self.d
    def getFinal(self):
        return self.a
    def setVectorDistance(self, vectorDistance):
        self.vectorDistance = vectorDistance
    def getVectorDistance(self):
        return self.vectorDistance

def getMin(vectorDistance):
    min = sys.maxsize
    index = -2
    for i in range(0, len(vectorDistance)):
        if min > vectorDistance[i] and not vectorUsed[i]:
            min = vectorDistance[i]
            index = i
    vectorUsed[index] = True
    return index

file = open(sys.argv[1], "r")
arr = file.read()
file.close

lines = arr.split("\n")
params = lines[0].split(" ")

row = int(params[0])
column = int(params[1])
vehicles = int(params[2])
ride = int(params[3])
bonus = int(params[4])
steps = int(params[5])

lines.pop(0)

mat = []
res = dict()
i = 0
cpt = 0

ridesList = []
def computeDistance(ride1, ride2):
    return abs(ride1.getFinal().getX() - ride2.getDepart().getX()) + abs(ride1.getFinal().getY() - ride2.getDepart().getY())

i = 0


#def init():

global vectorUsed

global vehiculeUsed

vectorUsed = []

vehiculeUsed = []

for line in lines:
    if ( not line):
        break
    params = line.split(' ')
    ridesList.append(Ride(i, Point(int(params[0]), int(params[1])), Point(int(params[2]), int(params[3])), int(params[4])))
    vectorUsed.append(False)
    i += 1

for i in range(0, len(ridesList)):
    vectorDistance = []
    print(i)
    for j in range(0, len(ridesList)):
        vectorDistance.append(computeDistance(ridesList[i], ridesList[j]))
    ridesList[i].setVectorDistance(vectorDistance)

r0 = Ride(-1, Point(0, 0), Point(0, 0), 0)

r0vectorDistance = []

for i in range(0, len(ridesList)):
    r0vectorDistance.append(computeDistance(r0, ridesList[i]))
r0.setVectorDistance(r0vectorDistance)

# # Print MAtrix distance
# for i in range(0, len(r0vectorDistance)):
#     print(r0vectorDistance[i])



# # Print MAtrix distance
# for i in range(0, len(ridesList)):
#     print(ridesList[i].getVectorDistance())

maxRide = int(ride / vehicles)

for i in range(0, vehicles):
    res.setdefault(i, []).append(getMin(r0.getVectorDistance()))

for i in range(0, vehicles):
    for j in range(1, maxRide):
        rPrev = ridesList[res[i][len(res[i]) - 1]]
        min = getMin(rPrev.getVectorDistance())
        if min == -2:
            break
        res[i].append(min)

file = open(sys.argv[1].split(".")[0] + ".out", "w")
for key, value in res.items():
    string = str("")
    for val in value:
        string += str(val) + " "
    file.write(str(len(value)) + " " + str(string) + "\n")