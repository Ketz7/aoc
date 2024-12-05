import functools

file = open(r"input_5.txt")

rules = []

for line in file:
    if line.isspace(): break
    rules.append(list(map(int, line.split("|"))))

cache = {}

for x,y in rules:
    cache[(x,y)] = True
    cache[(y,x)] = False

cache_2 =  {}

for x,y in rules:
    cache_2[(x,y)] = -1
    cache_2[(y,x)] = 1

def is_ordered_2(update):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            key = (update[i], update[j])
            if key in cache_2 and cache_2[key] == 1:
                return False
    return True

def cmp(x,y):
    return cache_2.get((x,y), 0)

def is_ordered(update):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            key = (update[i], update[j])
            if key in cache and not cache[key]:
                return False
    return True

total = 0

total_2 = 0 

for line in file:
    update = list(map(int, line.split(",")))
    if is_ordered(update):
        total += update[len(update) // 2]
    if is_ordered_2(update): continue
    update.sort(key=functools.cmp_to_key(cmp))
    total_2 += update[len(update) // 2]

print(total)
print(total_2)