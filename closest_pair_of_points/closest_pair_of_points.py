import sys
import os
import math

current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_script_path))
if project_root not in sys.path:
    sys.path.append(project_root)

from time_measurement import time_function, CodeTimer

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

@time_function
def closest_pair_divide_conquer(points):
    if len(points) <= 3:
        return brute_force_closest_pair(points)

    points.sort(key=lambda x: x[0])

    mid = len(points) // 2
    left_points = points[:mid]
    right_points = points[mid:]

    left_closest, left_distance = closest_pair_divide_conquer(left_points)
    right_closest, right_distance = closest_pair_divide_conquer(right_points)

    min_distance = min(left_distance, right_distance)
    closest_pair = left_closest if left_distance < right_distance else right_closest

    strip_points = [point for point in points if abs(point[0] - points[mid][0]) < min_distance]
    strip_points.sort(key=lambda x: x[1])

    for i in range(len(strip_points)):
        j = i + 1
        while j < len(strip_points) and (strip_points[j][1] - strip_points[i][1]) < min_distance:
            distance = euclidean_distance(strip_points[i], strip_points[j])
            if distance < min_distance:
                min_distance = distance
                closest_pair = (strip_points[i], strip_points[j])
            j += 1

    return closest_pair, min_distance

def brute_force_closest_pair(points):
    min_distance = float('inf')
    closest_pair = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = euclidean_distance(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[i], points[j])

    return closest_pair, min_distance

points = [(1, 2), (3, 5), (7, 8), (4, 6), (9, 1), (2, 4)]

with CodeTimer('Closest Pair of Points'):
    result_divide_conquer = closest_pair_divide_conquer(points)

print("Divide and Conquer:")
print("Closest Pair:", result_divide_conquer[0])
print("Distance:", result_divide_conquer[1])
