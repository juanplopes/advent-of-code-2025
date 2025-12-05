import sys

ranges, answer1, answer2 = [], 0, 0
for line in sys.stdin.read().splitlines():
    if '-' in line:
        ranges.append(list(map(int, line.split('-'))))
        continue
    if line == '': continue
    answer1 += any(a <= int(line) <= b for a, b in ranges)

limit = min(a for a, b in ranges)
for a, b in sorted(ranges):
    answer2 += max(limit, b + 1) - max(limit, a)
    limit = max(limit, b + 1) 

print(answer1, answer2)