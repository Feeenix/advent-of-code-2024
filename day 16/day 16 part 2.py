import numpy as np
with open("day 16/input") as f:
    text = f.read().strip()
world = text.split("\n")
world = np.array([list(x) for x in world])
outworld = world.copy()
height = len(world)
width = len(world[0])
start = np.array((0,0))
end = np.array((0,0))
for y in range(height):
    for x in range(width):
        if world[y,x] == "S":
            start = np.array((x,y))
            print("\nFound the start at pos",x,y)
            break
    else:
        continue
    break
else:
    raise Exception("couldnt find start")
for y in range(height):
    for x in range(width):
        if world[y,x] == "E":
            end = np.array((x,y))
            print("\nFound the end at pos",x,y)
            break
    else:
        continue
    break
else:
    raise Exception("couldnt find end")

"""
  0
  n
3w e1
  s
  2
"""
def get_world(pos):
    return world[pos[1],pos[0]]
def rot_r(vec):
    return np.array(vec[1],-vec[0])
def rot_l(vec):
    return np.array(-vec[1],vec[0])
dirvectors = [
        np.array((0,-1)),
        np.array((1,0)),
        np.array((0,1)),
        np.array((-1,0))
        ]


# cost, node pos, rotation, log
open_nodes = [(0,start,1,[(0,start,1)])]
traversed = {}

i = 0
while True:
    i+=1
    open_nodes.sort(key=lambda x:-x[0])

    node = open_nodes.pop() 
    if node[1][0] == 3 and node[1][1] == 9 and node[2] == 0:
        pass
    if node[1][0] == 13 and node[1][1] == 1 and node[2] == 0:
        pass
    if node [2] > 143564+1:
        continue

    if (node[1][0],node[1][1],node[2]) in traversed and traversed[(node[1][0],node[1][1],node[2])] < node[0]:
        continue

    traversed[(node[1][0],node[1][1],node[2])] = node[0]
    
    outworld[node[1][1],node[1][0]] = "^>v<"[node[2]]
    
    if i % 10000 == 0:
        print("\n".join(["".join(line) for line in outworld]))
        print(node[0])
    
    if all(node[1] == end):
        
        print("Finished >",node[0],"<")
        setc = set()
        looknode = node
        while looknode[0]<= node[0]:
                   
            setc.update(set([(x[1][0],x[1][1]) for x in looknode[3]]))
            looknode = open_nodes.pop()
        print(len(setc))
        print("\n".join(["".join((char if (x,y) not in setc else "O") for x,char in enumerate(line)) for y,line in enumerate(world)]))
        break
    open_nodes.append((node[0]+1000,node[1],(node[2]+1)%4,node[3]+[(node[0]+1000,node[1],(node[2]+1)%4)]))
    open_nodes.append((node[0]+1000,node[1],(node[2]-1)%4,node[3]+[(node[0]+1000,node[1],(node[2]-1)%4)]))

    # try to go forward
    forwardpos = node[1]+dirvectors[node[2]]
    if get_world(forwardpos) != "#":
        open_nodes.append( (node[0]+1,forwardpos,node[2],node[3]+[(node[0]+1,forwardpos,node[2])]))
        # open_nodes.sort(key=lambda x:-x[0])
    else:
        # open_nodes.pop(0)
        pass


    # rightpos = node[1]+rot_r(dirvectors[node[2]])
    # if get_world(rightpos) != "#":
    #     open_nodes.append((node[0]+1000,rightpos,(node[2]+1)%4))
    # leftpos = node[1]+rot_l(dirvectors[node[2]])
    # if get_world(leftpos) != "#":
    #     open_nodes.append((node[0]+1000,leftpos,(node[2]-1)%4))
    
    


