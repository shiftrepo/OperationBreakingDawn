#!python3.6.8

from time import sleep
import sys
import random
import math
import copy
import tkinter

SCREEN_WIDTH = 360
SCREEN_HEIGHT = 360

POINTS_SIZE = 50
LOOP = 100000

def calc_distance(points, route):
  distance = 0
  for i in range(POINTS_SIZE):
    (x0, y0) = points[route[i]]
    if i == POINTS_SIZE - 1:
        (x1, y1) = points[route[0]]
    else:
        (x1, y1) = points[route[i+1]]
    distance = distance + math.sqrt((x0 -x1) * (x0 - x1) + (y0 - y1) * (y0 - y1))
  return distance

root = tkinter.Tk()
root.title(u"TSP Random")

root.geometry(str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT))

canvas = tkinter.Canvas(root, width = SCREEN_WIDTH, height = SCREEN_HEIGHT)
canvas.place(x=0, y=0)

points = []
for i in range(POINTS_SIZE):
    points.append((random.random(), random.random()))

route = list(range(POINTS_SIZE))

min_route = copy.copy(route)
min_dist = calc_distance(points, route)

for c in range(LOOP):
    #sleep(0.005)
    root.title(u"TSP Random (" + str(c + 1) + u"count)")

    random.shuffle(route)

    dist = calc_distance(points, route)

    if min_dist > dist:
        min_route = copy.copy(route)
        min_dist = dist

        canvas.delete('all')
        for i in range(POINTS_SIZE):
            (x0, y0) = points[route[i]]
            if i == POINTS_SIZE - 1:
                (x1, y1) = points[route[0]]
            else:
                (x1, y1) = points[route[i+1]]

            canvas.create_line(x0 * SCREEN_WIDTH, y0 * SCREEN_HEIGHT, x1 * SCREEN_WIDTH, y1 * SCREEN_HEIGHT, fill="black", width=1)

            canvas.create_oval(x0 * SCREEN_WIDTH - 3, y0 * SCREEN_HEIGHT - 3, x0 * SCREEN_WIDTH + 3, y0 * SCREEN_HEIGHT + 3, fill="blue")

        canvas.create_text(5, 5, text = "{:.2f}".format(min_dist), anchor = "nw", fill = "red")
        canvas.update()

root.mainloop()