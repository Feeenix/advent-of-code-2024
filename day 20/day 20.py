with open("day 20/input") as f:
    text = f.read().strip() 
    
maze = [list(a) for a in text.split("\n")]
height = len(maze)
width = len(maze[0])
end = None
start = None
# finner start og sluttpunkter
for y in range(height):
    for x in range(width):
        if maze[y][x] == "S":
            start = (x,y)
        if maze[y][x] == "E":
            end = (x,y)
assert (not end is None ) and (not start is None)
# traverserer gjennom og finner hvor lang tid det tar å komme til et punkt
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
count = 0 # ser etter to tall på motsatt side av vegger og bruker de til å finne ut hvor mye tid man sparer
for y in range(1,height-1):
    for x in range(1,width-1):
        if (x,y) == (6,7):
            pass
        if maze[y][x] == "#":#sjekker om det er vegg
            # check adjacents
            save = 0
            if maze[y+1][x] != "#" and maze[y-1][x] != "#": # sjekker på vertikalen
                save = max(save, abs(locations[(x,y+1)]-locations[(x,y-1)])-2)
            if maze[y][x+1] != "#" and maze[y][x-1] != "#": # sjekker på horisontalen
                save = max(save, abs(locations[(x+1,y)]-locations[(x-1,y)])-2)
            if save >= 100:
                count += 1
print(count)














    