import json

with open('input_day01.txt') as f:
    content = f.read()  
    lines = content.splitlines()  


# Day 1 P 1

a, b = [], []
for line in lines:
    num1, num2 = map(int, line.split())
    a.append(num1)
    b.append(num2)

a_sort = sorted(a)
b_sort = sorted(b)

subtraction = [abs(x - y) for x,y in zip(a_sort,b_sort)]

print("Day 1, Part 1 Answer: ", sum(subtraction))

# Day 1 P 2

hashmap = {x: (b.count(x), a.count(x)) for x in a if b.count(x) > 0}

result = {key: key * (value[0] * value[1]) for key,value in hashmap.items()}

total_sum = sum(result.values())

print("Day 1, Part 2 Answer: ", total_sum)