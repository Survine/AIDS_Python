import math

def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance


x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

point_a = (x1, y1)
point_b = (x2, y2)

distance = calculate_distance(point_a, point_b)
print(f"The distance between {point_a} and {point_b} is {format(distance, '.2f')}")