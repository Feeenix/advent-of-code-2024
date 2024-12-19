with open("day 18/input") as f:
    text = f.read().strip()

allwalls = [(tuple(map(int,line.split(",")))) for line in  text.split("\n")]
wallnum = 0
walls = set()
start = (0,0)
end = (70,70)

previous_added = None

def sumv(v1,v2):
    return (v1[0]+v2[0],v1[1]+v2[1])
def dist(v1,v2):
    return ((v1[0]-v2[0])**2+(v1[1]-v2[1])**2)

while True:
    search_space = [(start,0,70*70+70*70,set((start,)))]
    space_gotten_to = {}
    travel_path = set()
    k = 0
    is_connected = False
    while search_space: #  while loop to check for connectedness
        search_space.sort(key=lambda x:x[1],reverse=True)
        focus = search_space.pop()
        if k%1000 == 0:
            pass
        k+=1
        if focus[0]==end:
            travel_path = focus[3].copy()
            is_connected = True
            break
        if focus[0][0]<0 or focus[0][0]>70 or focus[0][1]<0 or focus[0][1]>70 :
            continue
        if focus[0] in walls:
            continue
        if not focus[0] in space_gotten_to:
            space_gotten_to[focus[0]] = focus[1]
        if space_gotten_to[focus[0]] >= focus[1]:
            space_gotten_to[focus[0]] = focus[1]
        else:
            continue
        for vector in [(-1,0),(0,-1),(1,0),(0,1)]:
            sumvector = sumv(focus[0],vector)
            if not sumvector in space_gotten_to:
                space_gotten_to[sumvector] = focus[1]+1
            else: continue
            if space_gotten_to[sumvector] >= focus[1]+1:
                space_gotten_to[sumvector] = focus[1]+1
            search_space.append((sumvector,focus[1]+1,dist(end,sumvector),focus[3] | set((sumvector,))))
        
        
        
    if not is_connected:
        print(",".join(map(str,previous_added))) # <-- Output
        break
    
    
    while True: # add things until they hit the path, once they do, check for connectedness once more
        previous_added = allwalls[wallnum]
        wallnum+=1
        walls.add(previous_added)
        if previous_added in travel_path:
            break
        
    



pass

