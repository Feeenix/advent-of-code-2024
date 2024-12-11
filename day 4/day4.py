import numpy as np

def count_xmas(data):
    count = 0
    for line in data:
        for i in range(0, len(line)-3):
            if line[i:i+4] == ('X','M','A','S'):
                count += 1
    pass           
    for j in range(0,len(data)-3):
        for i in range(0, len(data[0])-3):
            # print(data[j][i],data[j+1][i+1],data[j+2][i+2],data[j+3][i+3])
            if data[j][i] == 'X' and data[j+1][i+1] == 'M' and data[j+2][i+2] == 'A' and data[j+3][i+3] == 'S':
                count += 1
    return count
with open("day 4/input") as f:
    data = f.read().strip()
    
    data = [list(line) for line in data.split("\n")]
    sum_ = 0
    for i in range(4):
        data = list(zip(*data))[::-1]
        sum_ += count_xmas(data)
    # rotated = list(zip(*data))[::-1]
    
    
    print(sum_)
    
    
    
    
    
    
    
    
    
    
    pass