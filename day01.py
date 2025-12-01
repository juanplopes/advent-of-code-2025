import sys
def solve(line):
    return (-1 if line[0] == 'L' else 1) * int(line[1:])
    
state, answer1, answer2 = 50, 0, 0
for line in sys.stdin.read().splitlines():
    clicks = solve(line)
    for i in range(abs(clicks)):
        state += 1 if clicks > 0 else -1
        state %= 100
        if state == 0: answer2 += 1
    if state == 0: answer1 += 1
#    print(' ', state)
    
print(answer1, answer2)