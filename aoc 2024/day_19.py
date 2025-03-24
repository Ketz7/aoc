with open('input.txt') as f:
    s = f.read().strip()

P1 = P2 = 0

s1, s2 = s.split('\n\n')

s1 = set(s1.split(", "))

cache = {}
def solve(s):
    if s not in cache:
        if len(s) == 0:
            return 1
        else:
            result = 0
            for poss in s1:
                if s.startswith(poss):
                    result += solve(s[len(poss) :])
                cache[s] = result
    return cache[s]


# P1
for l in s2.split("\n"): 
    if solve(l) > 0:
       P1 += 1

# P2 
for l in s2.split("\n"):
    P2 += solve(l) 


print(f"Part One: {P1}")
print(f"Part Two: {P2}")