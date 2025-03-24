grid = open("sample_4.txt").read().splitlines()

# P 1

p1_count = 0

print(len(grid))
print(grid)

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] != "X": continue
        for dr in [-1,0,1]:
            for dc in [-1,0,1]:
                if dr == dc == 0 :continue
                if not (0 <= r + 3 * dr < len(grid) and 0 <= c + 3 * dc < len(grid[0])): continue
                print(grid[r + dr][c + dc])

# for r in range(len(grid)):
#     for c in range(len(grid[0])):
#         if grid[r][c] != "X": continue
#         for dr in [-1,0,1]:
#             for dc in [-1,0,1]:
#                 if dr == dc == 0: continue
#                 if not (0 <= r + 3 * dr < len(grid) and 0 <= c + 3 * dc < len(grid[0])): continue
#                 if grid[r + dr][c + dc] == "M" and grid[r + 2 * dr][c + 2 * dc] == "A" and grid[r + 3 *dr][c + 3 * dc] == "S":
#                     p1_count += 1

# print(p1_count)

# # P 2
 
# p2_count = 0

# for r in range(1, len(grid) - 1):
#     for c in range(1, len(grid[0]) - 1):
#         if grid[r][c] != "A": continue
#         corners = [grid[r -1 ][c - 1], grid[r - 1][c + 1], grid[r + 1][c + 1], grid[r+ 1][c -1] ]
#         if "".join(corners) in ["MMSS", "MSSM", "SSMM", "SMMS"]:
#             p2_count += 1

# print(p2_count)

# import re
# f=re.findall
# print(len(re.findall("(?s)(?<=M.S.{139})A(?=.{139}M.S)|(?<=M.M.{139})A(?=.{139}S.S)|(?<=S.S.{139})A(?=.{139}M.M)|(?<=S.M.{139})A(?=.{139}S.M)",i:=open('input_4.txt').read())),len(f("(?s)(?<=SAM)(?=X)|X(?=MAS)|(?<=S.{140}A.{140})(?=M.{140}X)|(?<=X.{140})M(?=.{140}A.{140}S)|(?<=S.{141})(?=A.{141}M.{141}X)|(?<=X.{141}M.{141})A(?=.{141}S)|(?=S.{139}A.{139}M.{139}X)|(?<=X.{139}M.{139}A.{139})S",i)))