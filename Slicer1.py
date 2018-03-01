#!/usr/bin/python

import sys

file = open(sys.argv[1], "r")
arr = file.read()
file.close

lines = arr.split("\n")
params = lines[0].split(" ")

r = int(params[0])
c = int(params[1])
l = int(params[2])
h = int(params[3])

lines.pop(0)

mat = []
res = []

for line in lines:
    tmp = []
    for char in line:
        tmp.append(char)
    mat.append(tmp)


def form(size):
    ret = [(1,1)]
    while size > 1:
        i = 1
        tmp = size
        while tmp > 0:
            if (tmp, i) not in ret:
                ret.append((tmp, i))
            i += 1
            tmp = size / i
        size -= 1
    return ret


rect_all = form(h)

for y in range(0, r):
    for x in range(0, c):
        for rect in rect_all:
            t = 0
            m = 0
            over = False
            for i in range(0, rect[0]):
                if x + i >= c:
                    over = True
                else:
                    for j in range(0, rect[1]):
                        if y + j >= r:
                            over = True
                        else:
                            if mat[y+j][x+i] == 'M':
                                m += 1
                            elif mat[y+j][x+i] == 'T':
                                t += 1
                            else:
                                over = True
            if not over:
                if m >= l and t >= l:
                    res.append((y, x, y+rect[1]-1, x+rect[0]-1))
                    for i in range(0, rect[0]):
                        for j in range(0, rect[1]):
                            mat[y+j][x+i] = ''
                    break


file = open(sys.argv[1].split(".")[0] + ".out", "w")

file.write(str(len(res)) + "\n")
for res_rect in res:
    file.write(str(res_rect[0]) + " " + str(res_rect[1]) + " " + str(res_rect[2]) + " " + str(res_rect[3]) + "\n")

file.close()



