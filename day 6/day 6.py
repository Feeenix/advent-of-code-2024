

def rotate_cw(matrix): # cw
    return list(zip(*matrix[::-1]))
def rotate_ccw(matrix): # ccw
    return list(zip(*matrix))[::-1]



with open("day 6/input") as f:
    lines = f.read().strip()
unique_locations = set()
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
unique_locations.add((x,y))
world_out[y][x] = "X"
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
    
    
    
    # if direction == 0:
    #     return y,width-1-x
    # if direction == 1:
    #     return width-1-x,height-1-y
    # if direction == 2:
    #     return height-1-y, x
    # if direction == 3: 
    #     return x, y
    raise Exception()


def v(dir):
    return [[0,-1],[1,0],[0,1],[-1,0]][dir]


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
        x += ux
        y += uy
        unique_locations.add((x,y))
        world_out[y][x] = "X"
    
    direction = (direction+1)%4
    if end:
        break
    
    
    
    
print(len(unique_locations))
    
    
    
    
    


















pass