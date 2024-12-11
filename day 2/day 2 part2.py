amount_safe = 0

for line in open('day 2/input').readlines():
    line = line.split()
    line = [int(i) for i in line]
    
    for j in range(len(line)):
        new_line = line.copy()
        new_line.pop(j)
        is_increasing = -1
        if new_line[0] < new_line[1]:
            is_increasing = 1 
        elif new_line[0] == new_line[1]:
            continue
        
        for i in range(1,len(new_line)):
            diff = new_line[i] - new_line[i-1]
            if diff == 0:
                break
            if abs(diff) > 3:
                break
            if diff * is_increasing<0:
                break
        else: # this happens if the loop completes without breaking
            
            ...
            amount_safe += 1
            
            break
    else:
        continue
    
print(amount_safe)
            