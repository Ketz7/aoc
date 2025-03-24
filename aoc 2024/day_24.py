input = open('input.txt').read()
parts = input.split('\n\n')
values = {}
for line in parts[0].splitlines(keepends=False):
    c, v = line.split(': ')
    values[c] = int(v)
cons = {}
for line in parts[1].splitlines(keepends=False):
    a, op, b, _, c = line.split()  # x08 AND y08 -> hdk
    cons[c] = a, op, b

while True:
    again = False
    for c, (a, op, b) in cons.items():
        if c not in values and a in values and b in values:
            if op == "AND":
                values[c] = values[a] & values[b]
            elif op == "OR":
                values[c] = values[a] | values[b]
            elif op == "XOR":
                values[c] = values[a] ^ values[b]
            again = True
    if not again:
        break
print("Part 1:", sum(v * 2**i for i, v in enumerate(map(values.get, sorted(c for c in values if c[0] == 'z')))))

def find(a, op, b=None):
    if b:
        for c in cons:
            if cons[c] in ((a, op, b), (b, op, a)):
                return c
    else:
        for c in cons:
            if op == cons[c][1]:
                if a == cons[c][0]:
                    return c, cons[c][2]
                elif a == cons[c][2]:
                    return c, cons[c][0]

def swap(a, b):
    cons[a], cons[b] = cons[b], cons[a]
    wrongs.update({a, b})

wrongs = set()
a = find(f"x00", "AND", f"y00")
for i in range(1, 45):
    x = f"x{i:02}"
    y = f"y{i:02}"
    z = f"z{i:02}"
    c_maybe = find(x, "XOR", y)
    z_maybe, c = find(a, "XOR")
    if z != z_maybe:
        swap(z, z_maybe)
    if c != c_maybe:
        swap(c, c_maybe)
    d_maybe = find(x, "AND", y)
    e_maybe = find(c, "AND", a)
    a_maybe = find(d_maybe, "OR", e_maybe)
    a = a_maybe  # huh?
print("Part 2:", ','.join(sorted(wrongs)))