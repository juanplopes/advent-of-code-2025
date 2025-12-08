import sys, math

answer1, answer2 = 0, 0
T = sys.stdin.read().splitlines()
ops = T[-1].split()
nums1, nums2 = list(map(str.split, T[:-1])), [[]]

for i in range(len(T[0])):
    v = ''.join(T[j][i] for j in range(len(T) - 1) if T[j][i] != ' ')
    if v == '': nums2.append([])
    else:       nums2[-1].append(v)

for i, op in enumerate(ops):
    fn = {'+': sum, '*': math.prod}[op]
    answer1 += fn(int(nums1[j][i]) for j in range(len(nums1)))
    answer2 += fn(int(nums2[i][j]) for j in range(len(nums2[i])))

print(answer1, answer2)