def rotate_cw(matrix): # cw
    return list(zip(*matrix[::-1]))
def rotate_ccw(matrix): # ccw
    return list(zip(*matrix))[::-1]
with open("day 6/input") as f:
    lines = f.read().strip()
unique_locations = {}
world = lines.split("\n")
world_out = [(list(line)) for line in world]
world = [tuple(list(line)) for line in world]

height = len(world)
width = len(world[0])

direction = 0
x,y = 0,0
# find location
for i in range(len(world)):
    try:
        x = world[i].index("^")
        y = i
        break
    except:
        continue
    
startx,starty = x,y
unique_locations[(x,y)] = direction
world_out[y][x] = "|-|-"[direction]
right_direction_world = rotate_cw(world)


worldrotations = {0: right_direction_world,
                  1: world,
                  2: rotate_cw(rotate_cw(right_direction_world)),
                  3: rotate_cw(right_direction_world)
    }

def indexfromxyd(x,y,direction,width=width-1, height=height-1):
    if direction == 0:
        return height-y, x
    if direction == 1:
        return x, y
    if direction == 2:
        return y,width-x
    if direction == 3: 
        return width-x,height-y
    raise Exception()
def v(dir):
    return [[0,-1],[1,0],[0,1],[-1,0]][dir]


def test_if_loop(ox,oy,x,y,direction):
    if (ox,oy) == (startx,starty):
        return False
    
    if (ox,oy) == (8,1):
        pass
    thisworld = world.copy()
    thisworld = [list(x) for x in thisworld]
    thisworld[oy][ox] = "#"
    right_direction_world_ = rotate_cw(thisworld)


    worldrotations_ = {0: right_direction_world_,
                    1: thisworld,
                    2: rotate_cw(rotate_cw(right_direction_world_)),
                    3: rotate_cw(right_direction_world_)}
    
    
    unique_locations_ = set()
    loops = False
    prev4 = [None,None,None,None]
    while True:
        # unique_locations_[x,y] = direction
        i,j = indexfromxyd(x,y,direction)
        char_pos = i #worldrotations_[direction][j].index("^")
        end = False
        try:
            wall_pos = worldrotations_[direction][j][char_pos:].index("#")
        except:
            wall_pos = len(worldrotations_[direction][j][char_pos:])
            break
        traverselength = wall_pos
        
        ux,uy = v(direction)
        
        for k in range(traverselength-1):
            
            if (x,y,direction) in unique_locations_ :
                loops = True
                break         
            unique_locations_.add((x,y,direction))   
            thisworld[y][x]="X"
            x += ux
            y += uy
            
        else:
            if (x,y,direction) in unique_locations_:
                loops = True
                break
            unique_locations_.add((x,y,direction))   
            
            # if prev4[3] == (x,y,direction):
            #     loops = True
            #     break
            prev4.insert(0,(x,y,direction))
            prev4 = prev4[0:100]
            
            
            
            direction = (direction+1)%4
            if end:
                break
            continue
        break
    return loops



obstacle_locations = set()


while True:
    i,j = indexfromxyd(x,y,direction)
    char_pos = i #worldrotations[direction][j].index("^")
    end = False
    try:
        wall_pos = worldrotations[direction][j][char_pos:].index("#")
    except:
        wall_pos = len(worldrotations[direction][j][char_pos:])
        end = True
        
    traverselength = wall_pos
    
    ux,uy = v(direction)
    
    for k in range(traverselength-1):
        if test_if_loop(x+ux,y+uy,startx,starty,0):
            obstacle_locations.update({(x+ux,y+uy)})
        
        
        x += ux
        y += uy
        unique_locations[(x,y)] = direction
        world_out[y][x] = "|-|-"[direction]
    
    direction = (direction+1)%4
    if end:
        break
    
    
    
    
print(len(obstacle_locations))
    
    
    
    
    


















pass

pass