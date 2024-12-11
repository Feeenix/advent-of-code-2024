amount_safe = 0

for line in open('day 2/input').readlines():
    line = line.split()
    line = [int(i) for i in line]
    is_increasing = -1
    if line[0] < line[1]:
        is_increasing = 1 
    elif line[0] == line[1]:
        continue
    
    for i in range(1,len(line)):
        diff = line[i] - line[i-1]
        if diff == 0:
            break
        if abs(diff) > 3:
            break
        if diff * is_increasing<0:
            break
    else: # this happens if the loop completes without breaking
        
        ...
        amount_safe += 1
        
        continue
    continue

print(amount_safe)
            