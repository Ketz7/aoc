from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y,
        )


DIRECTIONS = [
    Point(-1, 0),
    Point(0, 1),
    Point(1, 0),
    Point(0, -1),
]

FULL_DIRECTIONS = {
    (Point(-1, 0), Point(0, 1)): Point(-1, 1),
    (Point(0, 1), Point(1, 0)): Point(1, 1),
    (Point(1, 0), Point(0, -1)): Point(1, -1),
    (Point(0, -1), Point(-1, 0)): Point(-1, -1),
}


map = {}
input_ = open('input_6.txt').read()
for y, row in enumerate(input_.splitlines()):
    for x, cell in enumerate(row):
        map[Point(x, y)] = cell

perimeters = {}
regions = []

points = set(map)


while points:
    region = set()
    point = points.pop()
    plant = map[point]
    region.add(point)
    corners = 0

    points_to_check = [point]
    while points_to_check:
        next_point = points_to_check.pop()
        points.discard(next_point)
        perimeter = 0

        for (dir_left, dir_right), dir_middle in FULL_DIRECTIONS.items():
            sur_point_left = next_point + dir_left
            sur_point_right = next_point + dir_right
            sur_plant_left = map.get(sur_point_left)
            sur_plant_right = map.get(sur_point_right)
            if plant not in (sur_plant_left, sur_plant_right):
                corners += 1
                continue
            if (
                    sur_plant_left == plant
                    and sur_plant_right == plant
            ):
                sur_point_middle = next_point + dir_middle
                sur_plant_middle = map.get(sur_point_middle)
                if sur_plant_middle != plant:
                    corners += 1


        sur_points = []
        for dir_ in DIRECTIONS:
            sur_points.append(next_point + dir_)
        for sur_point in sur_points:
            if map.get(sur_point) == plant:
                if sur_point not in region:
                    region.add(sur_point)
                    points_to_check.append(sur_point)
            else:
                perimeter += 1
        perimeters[next_point] = perimeter

    regions.append((region, plant, corners))


prices_1 = 0
prices_2 = 0
for region, _, corners in regions:
    area = len(region)

    perimeter = 0
    for point in region:
        perimeter += perimeters[point]

    price_1 = area * perimeter
    prices_1 += price_1

    price_2 = area * corners
    prices_2 += price_2

print(prices_1)
print(prices_2)