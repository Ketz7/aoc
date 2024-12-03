import re

with open('input_3.txt') as f:
    content = f.read().strip()

# P 1
data = re.findall(r'mul\((\d+,\d+)\)', content)

result = sum(int(x) * int(y) for pair in data for x,y in [pair.split(',')])

print('Part 1: ', result)

# P 2

data2 = re.findall(r"do\(\)|'t\(\)|l\(\d+,\d+\)", content)

content = re.sub(r"don't\(\).*?(?:$|do\(\))", '', content, flags=re.DOTALL)

result = sum(int(a)*int(b) for a,b in re.findall(r'mul\((\d+),(\d+)\)', content))

print('Part 2: ', result)
