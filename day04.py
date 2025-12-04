import sys, functools

def remove(T):
    S = {(i, j) for i in range(len(T)) for j in range(len(T[i])) if T[i][j] == '@'}
    for (i, j) in S:
        if sum((i+a, j+b) in S for a in (-1,0,1) for b in (-1,0,1)) < 5:
            yield 1
            T[i][j] = '.'

T = [list(s) for s in sys.stdin.read().splitlines()]
answers = [sum(remove(T))]
while answers[-1] != 0:
    answers += [sum(remove(T))]

print(answers[0], sum(answers))