
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

lines.pop(0)
lines.pop()
rides = []
for line in lines:
    tmp = []
    for num in line.split(" "):
        tmp.append(int(num))
    rides.append(tmp)


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])



def timend(car, rid, end):
    return max(car[2] + distance(car, rid), rid[4]) + distance(rid, end)


def waitime(car, rid):
    return rid[4] - (car[2] + distance(car, rid))

def ridepoint(rid):
    tmp = (rid[2], rid[3])
    return distance(tmp, rid)


def get_result():
    car_pos = []
    res = []
    for vehicule in range(0, vehicules):
        car_pos.append((0, 0, 0))
        res.append([])

    while True:
        best_ride_car = []
        smallest = None
        for i in range(0, len(rides)):
            ride = rides[i]
            min = 10000
            best = None
            if ride is not None:
                pos_end = (ride[2], ride[3])
                for veh in range(0, vehicules):
                    wait = waitime(car_pos[veh], ride)
                    if wait < 0:
                        wait = 0
                    dist = distance(car_pos[veh], ride) + wait


                    if dist < min and timend(car_pos[veh], ride, pos_end) <= ride[5]:
                        min = dist
                        best = (veh, i, dist)
                if best is not None:
                    if smallest is None:
                        smallest = best[2]
                    if smallest > best[2]:
                        best_ride_car.append(best)
            if len(best_ride_car) > 100:
                break


        if not best_ride_car:
            break
        print len(best_ride_car)
        small_dist = (0, best_ride_car[0][2])
        min_best = best_ride_car[0]
        inc = 0
        for b in best_ride_car:
            if b[2] < small_dist[1]:
                small_dist = (inc, b[2])
                min_best = b
            inc += 1

        res[min_best[0]].append(min_best[1])

        pos_end = (rides[min_best[1]][2], rides[min_best[1]][3])
        car_pos[min_best[0]] = (rides[min_best[1]][2], rides[min_best[1]][3], timend(car_pos[min_best[0]], rides[min_best[1]], pos_end))
        rides[min_best[1]] = None

    return res


result = get_result()

file = open(sys.argv[1].split(".")[0] + ".out", "w")

for res in result:
    file.write(str(len(res)))
    for r in res:
        file.write(" " + str(r))
    file.write("\n")

file.close()