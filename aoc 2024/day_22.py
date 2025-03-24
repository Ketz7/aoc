import sys, re
from collections import Counter, deque

with open('input.txt') as file:
    content = file.read()

def ints(s: str) -> tuple[int, ...]:
    return tuple(map(int, re.findall(r'\d+', s)))

def evolve(n):
    n = (n ^ (n << 6)) & 16777215
    n = (n ^ (n >> 5)) & 16777215
    n = (n ^ (n << 11)) & 16777215
    return n

def apply_n_times(fn, n, x):
    for _ in range(n):
        x = fn(x)
    return x

def evaluate_sequences(number: int) -> Counter[tuple[int, int, int, int]]:
    value_table = Counter()
    window = deque(maxlen=4)
    price = number % 10
    for _ in range(2000):
        number = evolve(number)
        last_price, price = price, number % 10
        window.append(price - last_price)
        sequence = tuple(window)
        if len(sequence) < 4 or sequence in value_table:
            continue
        value_table[sequence] = price
    return value_table

numbers = ints(content)

p1 = sum(apply_n_times(evolve, 2000, number) for number in numbers)
print(p1)

bananas_by_sequence = sum(map(evaluate_sequences, numbers), start=Counter())
best_sequence, best_value = bananas_by_sequence.most_common(1)[0]
print(best_sequence, best_value)