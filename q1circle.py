import math
from math import sqrt


def solution(s: str, x: list, y: list):
    """
    solves q1. grabs as many points with circle center being at (0, 0).
    the k-th point is: s[k], x[k], y[k].
    all lists assumed same size.
    roughly O(n log n) "base 2"
    :param s: letter tags str.
    :param x: x coordinate list
    :param y: y coordinate list
    :return:
    """
    # note: could put safety checks
    points_grabbed = 0

    # create list of points
    points_list = []
    for i in range(len(s)):
        distance = distance_from_origin((x[i], y[i]))

        # note: way better to use class
        point = (x[i], y[i], s[i], distance)
        points_list.append(point)

    # sort by distance
    points_list.sort(key=lambda p: p[3])

    # grab points one at a time
    tabs_grabbed = set()
    for i, point in enumerate(points_list):
        tag = point[2]
        distance = point[3]

        # we are beyond the circle's edge
        if tag in tabs_grabbed:
            i -= 1
            # remove all grabbed points at the outer edge
            while i >= 0:
                prev_point = points_list[i]
                prev_distance = prev_point[3]

                if math.isclose(prev_distance, distance):
                    points_grabbed -= 1
                else:
                    break

                i -= 1
            break
        else:
            tabs_grabbed.add(tag)
            points_grabbed += 1

    return points_grabbed


def distance_from_origin(point: tuple):
    """
    :param point: (x,y) coordinates
    :return:
    """
    x, y = point
    c_squared = x ** 2 + y ** 2
    return sqrt(c_squared)
