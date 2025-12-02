import sys

answer1, answer2 = 0, 0
for line in sys.stdin.read().split(','):
    a, b = line.split('-')
    for i in range(int(a), int(b)+1):
        s = str(i)
        ss = s+s

        if len(s)%2==0 and ss.find(s, len(s)//2) == len(s)//2: answer1 += i
        if 0 <= ss.find(s, 1) < len(s): answer2 += i
   
print(answer1, answer2)