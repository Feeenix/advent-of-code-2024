import numpy as np


with open("day 8/input") as f:
    world = f.read().strip().replace("#",".")
rows = world.count("\n")+1
flatworld = world.replace("\n","")
cols = len(flatworld)/rows
assert round(cols) == cols
cols = round(cols)
frequencies = set(list(flatworld))
frequencies.discard(".")
antennaelocations = {a: [] for a in frequencies}
def pos_to_xy(pos):
    return np.array([pos%cols,pos//rows])
def xy_to_pos(x,y):
    return y*cols+x

for i,a in enumerate(flatworld):
    # print(pos_to_xy(i))
    if a in antennaelocations:
        antennaelocations[a].append(i)


locations = set()

for freq in antennaelocations:
    antennae = antennaelocations[freq]
    length = len(antennaelocations[freq])
    for i in range(length):
        ipos = pos_to_xy(antennae[i])
        for j in range(i+1,length):
            jpos = pos_to_xy(antennae[j])
            pass
            ij_vec = jpos-ipos
            test_loc1 = ipos
            while True:
                test_loc1 = test_loc1+ij_vec
                if 0 <= test_loc1[0] < cols and 0<=test_loc1[1] < rows:
                    index_loc1 = xy_to_pos(*test_loc1)
                    locations.add((tuple(test_loc1)))
                    continue
                break
            test_loc2 = jpos
            while True:
                test_loc2 = test_loc2-ij_vec
                if 0 <= test_loc2[0] < cols and 0<=test_loc2[1] < rows:
                    index_loc2 = xy_to_pos(*test_loc2)
                    locations.add((tuple(test_loc2)))
                    continue
                break
            pass



print(len(locations))
pass