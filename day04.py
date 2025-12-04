import sys, functools

def remove(T):
    answer = 0
    M = {(i, j): T[i][j] == '@' for i in range(len(T)) for j in range(len(T[i]))}
    for (i, j) in M.keys():
        if T[i][j] != '@': continue
        if sum(M.get((i+a, j+b), 0) for a in range(-1, 2) for b in range(-1, 2) if a or b) < 4:
            answer += 1
            T[i][j] = '.'
    return answer


T = [list(s) for s in sys.stdin.read().splitlines()]
answers = [remove(T)]
while answers[-1] != 0:
    answers += [remove(T)]

print(answers[0], sum(answers))