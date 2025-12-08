import sys, math

T = sys.stdin.read().splitlines()
M = [[int(c == 'S') for c in l] for l in T]

answer1 = 0
for i in range(1, len(T)):
    for j in range(len(M[i])):
        if (T[i][j] != '^'):
            M[i][j] = (M[i-1][j] 
                + (M[i-1][j-1] if j-1 >= 0 and T[i][j-1] == '^' else 0) 
                + (M[i-1][j+1] if j+1 < len(M[i]) and T[i][j+1] == '^' else 0))
        else:
            answer1 += M[i-1][j] > 0

print(answer1, sum(M[-1]))
