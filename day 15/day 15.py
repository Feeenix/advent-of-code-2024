import numpy as np
with open("day 15/input") as f:
    text = f.read().strip()
world,moves = text.split("\n\n")
world = world.split("\n")
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

moves = moves.replace("\n","")
for i, move in enumerate(moves):
    if i%2000 == 0:
        # print("\n".join(["".join(line) for line in world]))
        print(i)
    
    ray = cursor.copy()
    doespush = False
    vector = [
        np.array((-1,0)),
        np.array((1,0)),
        np.array((0,-1)),
        np.array((0,1))
        ]["<>^v".index(move)]
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
                if item == "O": # optimization
                    if world[y+vector[1],x+vector[0]]=="#" and (world[y-vector[0],x+vector[1]]=="#" or world[y+vector[0],x-vector[1]]=="#"):
                        world[y,x] = "#"
                        out += y*100+x
                
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
        if world[y,x] == "O":
            out += y*100+x

print(out)
    
    


