import numpy as np

with open ("day 10/input", "r") as f:
    text = f.read().strip()

world = text.split("\n")
cols = len(world[0])
rows = len(world)

paths = {}
current_tip_id = 0

for y in range(rows):
    for x in range(cols):
        paths[(x,y)] = []
        if world[y][x] == "9":
            paths[(x,y)].append(current_tip_id)
            current_tip_id += 1

result = 0

for i in range(8,-1,-1): # 9 to 0
    for y in range(rows):
        for x in range(cols):
            if str(i) == world[y][x]:
                for vx,vy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    if 0<=x+vx<cols and 0<=y+vy<rows:
                        if str(i+1) == world[y+vy][x+vx]:
                            paths[(x,y)].extend(paths[(x+vx,y+vy)])
            if "0" == world[y][x]:
                result += len((paths[(x,y)])) # removed set() and that was part 2 done
                

print(result)
pass
    
    








    