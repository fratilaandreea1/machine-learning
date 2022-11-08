import math

from matplotlib import pyplot as plt
import random

from Point import Point

colors = ['pink', 'purple', 'yellow']
zona1 = [180, 220, 10, 10]
zona2 = [-100, 110, 15, 10]
zona3 = [210, -150, 5, 20]
all_zones = [zona1, zona2, zona3]
# points = []
points_as_string = ""


def random_index():
    return random.randint(0, len(all_zones) - 1)


def G(coord, m, sigma):
    e = math.e

    a = (m - coord) ** 2
    b = 2 * (sigma ** 2)

    confidence = e ** (-a / b)

    return confidence.__round__(3)


def create_axes():
    plt.axhline(0)  # x-axis line
    plt.axvline(0)  # y-axis line
    plt.xlim(-300, 300)
    plt.ylim(-300, 300)
    for i in range(6000):
        get_coordinates()


def get_coordinates():
    index = random_index()
    random_zone = all_zones[index]

    x = random.randint(-300, 300)
    confidence = G(x, random_zone[0], random_zone[2])
    prg = random.random().__round__(3)
    while confidence < prg:
        x = random.randint(-300, 300)
        confidence = G(x, random_zone[0], random_zone[2])
        prg = random.random().__round__(3)

    y = random.randint(-300, 300)
    confidence = G(y, random_zone[1], random_zone[3])
    prg = random.random().__round__(3)
    while confidence < prg:
        y = random.randint(-300, 300)
        confidence = G(y, random_zone[1], random_zone[3])
        prg = random.random().__round__(3)

    point = Point(x, y, index)
    # points.append(Point(x, y))
    global points_as_string
    points_as_string += str(point)

    plt.plot(x, y, marker='.', color=colors[index], markersize=5)


create_axes()
file = open("coordinates.txt", "w+")
file.write(points_as_string)

plt.show()
