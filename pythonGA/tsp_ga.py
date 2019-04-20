#!python3.6.8

from time import sleep
import sys
import random
import math
import copy
import tkinter

SCREEN_WIDTH = 150
SCREEN_HEIGHT = 150

POINTS_SIZE = 50

POPULATION_SIZE = 20
GENERATION = 2000
MUTATE = 0.3
SELECT_RATE = 0.5

def calc_distance(points, route):
  distance = 0
  for i in range(POINTS_SIZE):
    (x0, y0) = points[route[i]]
    if i == POINTS_SIZE - 1:
        (x1, y1) = points[route[0]]
    else:
        (x1, y1) = points[route[i+1]]
    distance = distance + math.sqrt((x0 - x1) * (x0 - x1) + (y0 - y1) * (y0 - y1))
  return distance

def sort_fitness(points, population):
    fp = []
    for individual in population:
        fitness = calc_distance(points, individual)
        fp.append((fitness, individual))
    fp.sort()

    sorted_population = []

    for fitness, individual in fp:
        sorted_population.append(individual)

    return sorted_population

def selection(points, population):
    sorted_population = sort_fitness(points, population)
    n = int(POPULATION_SIZE * SELECT_RATE)
    return sorted_population[0:n]

def crossover(ind1, ind2):
    r1 = random.randint(0, POINTS_SIZE - 1)
    r2 = random.randint(r1 + 1, POINTS_SIZE)

    flag = [0] * POINTS_SIZE

    ind = [-1] * POINTS_SIZE

    for i in range(r1, r2):
        city = ind2[i]
        ind[i] = city

        flag[city] = 1

    for i in list(range(0, r1)) + list(range(r2, POINTS_SIZE)):

      city = ind1[i]

      if flag[city] == 0:
          ind[i] = city
          flag[city] = 1

    for i in range(0, POINTS_SIZE):
        if ind[i] == -1:
            for j in range(0, POINTS_SIZE):
                city = ind1[j]
                if flag[city] == 0:
                    ind[i] = city
                    flag[city] = 1
                    break
    return ind

def mutation(ind1):
    ind2 = copy.deepcopy(ind1)
    if random.random() < MUTATE:
        city1 = random.randint(0, POINTS_SIZE - 1)
        city2 = random.randint(0, POINTS_SIZE - 1)

        if city1 > city2:
            city1, city2 = city2, city1

        ind2[city1:city2+1] = reversed(ind1[city1:city2+1])

    return ind2

root = tkinter.Tk()
root.title(u"TSP GA")

width_size = 5

height_size = math.ceil(POPULATION_SIZE / width_size)

window_width = SCREEN_WIDTH * width_size

window_height = SCREEN_HEIGHT * height_size

root.geometry(str(window_width) + "x" + str(window_height))

canvas_list = []

for i in range(POPULATION_SIZE):
    canvas = tkinter.Canvas(root, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    cx = i % width_size * SCREEN_WIDTH
    cy = int(i / width_size) * SCREEN_HEIGHT
    canvas.place(x=cx, y=cy)
    canvas_list.append(canvas)

points = []
for i in range(POINTS_SIZE):
    points.append((random.random(), random.random()))

population = []
for i in range(POPULATION_SIZE):
    individual = list(range(POINTS_SIZE))
    random.shuffle(individual)
    population.append(individual)

for generation in range(GENERATION):
    root.title(u"TSP GA (" + str(generation + 1) + u") generation")

    population = selection(points, population)

    n = POPULATION_SIZE - len(population)
    for i in range(n):
        r1 = random.randint(0, len(population) - 1)
        r2 = random.randint(0, len(population) - 1)
        individual = crossover(population[r1], population[r2])

        individual = mutation(individual)

        population.append(individual)

    sort_fitness(points, population)

    for ind in range(POPULATION_SIZE):
        canvas = canvas_list[ind]
        route = population[ind]
        dist = calc_distance(points, route)
        canvas.delete('all')
        for i in range(POINTS_SIZE):
            (x0, y0) = points[route[i]]
            if i == POINTS_SIZE - 1:
                (x1, y1) = points[route[0]]
            else:
                (x1, y1) = points[route[i + 1]]

            canvas.create_line(x0 * SCREEN_WIDTH, \
                        y0 * SCREEN_HEIGHT, \
                        x1 * SCREEN_WIDTH, \
                        y1 * SCREEN_HEIGHT, \
                        fill="black", width=1)

            canvas.create_oval(x0 * SCREEN_WIDTH - 2, \
                        y0 * SCREEN_HEIGHT - 2, \
                        x0 * SCREEN_WIDTH + 2, \
                        y0 * SCREEN_HEIGHT + 2, \
                        fill="blue")

        canvas.create_rectangle(0, 0, SCREEN_WIDTH - 1, SCREEN_HEIGHT - 1, outline="gray", width=1)

        canvas.create_text(5, 5, text = "{:.2f}".format(dist), anchor = "nw", fill = "red")
        canvas.update()

root.mainloop()