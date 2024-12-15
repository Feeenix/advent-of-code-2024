import numpy as np
with open("day 15/input") as f:
    text = f.read().strip()
world,moves = text.split("\n\n")
world = world.replace("#","##").replace("O","[]").replace(".","..").replace("@","@.")
world = world.strip().split("\n")
world = np.array([list(x) for x in world])
height = len(world)
width = len(world[0])
cursor = np.array((0,0))
for y in range(height):
    for x in range(width):
        if world[y,x] == "@":
            cursor = np.array((x,y))
            print("\nFound the bot at pos",x,y)
            break
    else:
        continue
    break
else:
    raise Exception("couldnt find bot")
out = 0

canmove_memo = {}
def canmove(pos,vy):
    if (pos[0],pos[1],vy) in canmove_memo:
        return canmove_memo[(pos[0],pos[1],vy)]
    if world[pos[1],pos[0]] == "#":
        canmove_memo[(pos[0],pos[1],vy)] = False
        return False
    if world[pos[1],pos[0]] == ".":
        canmove_memo[(pos[0],pos[1],vy)] = True
        return True
    if world[pos[1],pos[0]] == "[":
        a = canmove((pos[0],pos[1]+vy),vy) and canmove((pos[0]+1,pos[1]+vy),vy)
        canmove_memo[(pos[0],pos[1],vy)] = a
        return a
    if world[pos[1],pos[0]] == "]":
        a = canmove((pos[0],pos[1]+vy),vy) and canmove((pos[0]-1,pos[1]+vy),vy)
        canmove_memo[(pos[0],pos[1],vy)] = a
        return a
# world_copy = world.copy()
def move(pos,vy):
    if world[pos[1],pos[0]] == "]": # remember what it was
        world[pos[1],pos[0]] = "."   # clear the floor as if jumping 
        world[pos[1],pos[0]-1] = "."
        move((pos[0],pos[1]+vy),vy) # while in the air, tell the boxes in front to do the same process as this one
        move((pos[0]-1,pos[1]+vy),vy)
        world[pos[1]+vy,pos[0]]="]" # when the other boxes have landed, it is cleared for us to land
        world[pos[1]+vy,pos[0]-1]="["
    if world[pos[1],pos[0]] == "[":# if it tries to push a left side of a box, tell it to push the right side instead
        move((pos[0]+1,pos[1]),vy)
    if world[pos[1],pos[0]] == "@": # if its the player, push it, but only in a single column
        world[pos[1],pos[0]] = "." # player acts like a small box
        move((pos[0],pos[1]+vy),vy)
        world[pos[1]+vy,pos[0]]="@"
    
moves = moves.replace("\n","")
for i, move_ in enumerate(moves):
    # if i%1 == 0:
    #     print("\n".join(["".join(line) for line in world]))
    #     print(i,move_)
    
    ray = cursor.copy()
    vector = [
        np.array((-1,0)),
        np.array((1,0)),
        np.array((0,-1)),
        np.array((0,1))
        ]["<>^v".index(move_)]
    if abs(vector[0]) == 0:
        canmove_memo = {}
        if canmove(cursor+vector,vector[1]):
            world_copy = world.copy()
            move(cursor,vector[1])
            cursor+=vector
    
    
    else:
        pushed = []
        while True:
            x,y = ray
            thing = world[y,x]
            if thing == "#":
                break
            if thing == ".":
                # world[cursor[1],cursor[0]] = "."
                for item in reversed(pushed):
                    world[y,x] = item
                    
                    
                    ray -= vector
                    x,y = ray
                world[y,x] = "."
                cursor+=vector

                break
            pushed.append(thing)
            # world[y,x] = "."
            ray += vector
    
print("\n".join(["".join(line) for line in world]))
    
    
# count gps

for y in range(height):
    for x in range(width):
        if world[y,x] == "[":
            out += y*100+x

print(out)
    
    


