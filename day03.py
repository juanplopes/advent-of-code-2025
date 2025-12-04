import sys

def solve(line, k):
    if k == 0: return ''
    first = max(line[:len(line)-k+1])
    return first + solve(line[line.index(first)+1:], k-1)

answer1, answer2 = 0, 0
for line in sys.stdin.read().splitlines():
    answer1 += int(solve(line, 2))
    answer2 += int(solve(line, 12))
   
print(answer1, answer2)