from itertools import product
from operator import add, mul

with open("input_6.txt", "r") as f:
    data = f.read().splitlines()


# Part 1
def calib(data: list[str], ops: tuple) -> int:
    total = 0
    for line in data:
        res, nums = line.split(": ")
        res, nums = int(res), tuple(int(x) for x in nums.split(" "))
        for inds in product(range(len(ops)), repeat=len(nums) - 1):
            i, tot = 1, ops[inds[0]](nums[0], nums[1])
            for j in inds[1:]:
                tot = ops[j](tot, nums[i + 1])
                i += 1
            if tot == res:
                total += res
                break
    return total


print(calib(data, (add, mul)))


# Part 2
def conc(a: int, b: int) -> int:
    return int(f"{a}{b}")


print(calib(data, (add, mul, conc)))