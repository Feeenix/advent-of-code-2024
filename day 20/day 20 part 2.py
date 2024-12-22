with open("day 20/testcase") as f:
    text = f.read().strip() 
    
maze = [list(a) for a in text.split("\n")]

height = len(maze)
width = len(maze[0])
end = None
start = None

for y in range(height):
    for x in range(width):
        if maze[y][x] == "S":
            start = (x,y)
        if maze[y][x] == "E":
            end = (x,y)
assert (not end is None ) and (not start is None)

# traverse
#bfs
v_list = [(0,1),(0,-1),(1,0),(-1,0)]
locations = {}
search_pool = [(start,0)]
while True:
    search_pool.sort(key=lambda x: x[1], reverse=True)    
    pos,cost = search_pool.pop()
    if maze[pos[1]][pos[0]] == "#":
        continue
    locations[pos] = cost
    if pos == end:
        break
    for v in v_list:
        new_pos = (pos[0]+v[0], pos[1]+v[1]) 
        if new_pos in locations:
            continue
        search_pool.append((new_pos,cost+1))

distmemo = {}
def taxicab_dist(a,b):
    if (a,b) in distmemo:
        return distmemo[(a,b)]
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def calculate_saved(pos1,pos2):
    if pos1 not in locations:
        return 0
    if pos2 not in locations:
        return 0
    return abs(locations[pos1]-locations[pos2])-taxicab_dist(pos1,pos2)

count = 0
for x,y in locations:
    for x2 in range(x-20,x+21):
        for y2 in range(y-20,y+21):
            dist = taxicab_dist((x,y),(x2,y2))
            if dist > 20:
                continue
            if not (x2,y2) in locations:
                continue
            if locations[(x,y)] > locations[(x2,y2)]: # search only one direction
                continue
            
            save = abs(locations[(x,y)]-locations[(x2,y2)])-dist


            if save >= 76:
                count += 1

# for y in range(1,height-1):
#     for x in range(1,width-1):
#         if (x,y) == (6,7):
#             pass
#         if maze[y][x] == "#":
#             # check adjacents
#             save = 0
#             if maze[y+1][x] != "#" and maze[y-1][x] != "#":
#                 save = max(save, abs(locations[(x,y+1)]-locations[(x,y-1)])-2)
#             if maze[y][x+1] != "#" and maze[y][x-1] != "#":
#                 save = max(save, abs(locations[(x+1,y)]-locations[(x-1,y)])-2)
            
#             # print(save)
#             if save >= 100:
#                 count += 1

    
    
        
print(count)














    