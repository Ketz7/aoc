from aoc_helper import *

import re

with open('input_3.txt') as f:
    content = f.read().strip()

# P 1
x = re.findall("mul\(\d+,\d+\)", content)

data = re.findall(r'mul\((\d+,\d+)\)', content)

result = sum(int(x) * int(y) for pair in data for x,y in [pair.split(',')])

print('Part 1: ', result)

# P 2
x = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", content)

ans = 0
g = True

for i in x:
    if i == 'do()':
        g = True
    elif i == "don't()":
        g = False
    else:
        if g:
            a, b = nums(i)
            ans += a * b
print(ans)

content = re.sub(r"don't\(\).*?(?:$|do\(\))", '', content, flags=re.DOTALL)

result = sum(int(x)*int(y) for x,y in re.findall(r'mul\((\d+),(\d+)\)', content))

print('Part 2: ', result)
