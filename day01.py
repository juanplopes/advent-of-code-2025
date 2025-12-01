import sys
    
state, answer1, answer2 = 50, 0, 0
for line in sys.stdin.read().splitlines():
    clicks = (-1 if line[0] == 'L' else 1) * int(line[1:])
    
    if clicks < 0: answer2 += abs((state + clicks-1) // 100) - (state == 0)
    elif clicks > 0: answer2 += abs((state + clicks) // 100)
    
    state = (state + clicks) % 100
    if state == 0: answer1 += 1
   
print(answer1, answer2)