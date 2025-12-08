import sys, collections, math, heapq

V = [list(map(int, l.split(','))) for l in sys.stdin.read().splitlines()]
E = [(sum((V[i][k]-V[j][k])**2 for k in range(3)) ** 0.5, i, j)
     for i in range(len(V)) for j in range(i+1, len(V))]
heapq.heapify(E)

P = list(range(len(V)))
def find(index):
    if P[index] == index: return index
    P[index] = find(P[index])
    return P[index] 

count1, count2, answer1, answer2 = 0, 0, 0, 0
while count2 < len(V)-1:
    _, i, j = heapq.heappop(E)

    count1 += 1
    if count1 == 1000: 
        answer1 = math.prod(heapq.nlargest(3, 
            collections.Counter(map(find, range(len(V)))).values()))

    a, b = find(i), find(j)
    P[min(a, b)] = max(a, b)
    if a != b: count2 += 1
    answer2 = V[i][0] * V[j][0]

print(answer1, answer2)
