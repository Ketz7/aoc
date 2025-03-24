import re

with open("input_6.txt") as f:
    text = f.read()
    blocks = text.split("\n\n")


def linearcombination(numbers, offset):
    xa, ya, xb, yb, x, y = numbers
    x, y = x + offset, y+offset
    b = round((((x/xa)-(y/ya))/((xb/xa)-(yb/ya))))
    a = round((x-(b*xb))/xa)
    return a*3 + b if a*xa + b*xb == x and a*ya + b*yb == y else 0


result = 0
result2 = 0
for block in blocks:
    pattern = r"(\d+)"
    numbers = list(map(int, re.findall(pattern, block)))
    result += linearcombination(numbers, 0)
    result2 += linearcombination(numbers, 10000000000000)
print(result)
print(result2)