import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
fig, ax = plt.subplots()
from colorsys import hsv_to_rgb

# ims is a list of lists, each row is a list of artists to draw in the
# current frame; here we are just animating one artist, the image, in
# each frame
def im_from_checked(checked,localchecked,world,width,height):
    im = []
    for y in range(height):
        im.append([])
        for x in range(width):
            im[y].append((0,0,0))
            if (x,y) in checked:
                r,g,b = hsv_to_rgb((hash(world[y][x])%(2**51)/(2**51)),0.7,0.6)
                
                
                im[y][x] = (int(r*255),int(g*255),int(b*255))
            if (x,y) in localchecked:
                r,g,b = hsv_to_rgb((hash(world[y][x])%(2**51)/(2**51)),1,1)
                im[y][x] = (int(r*255),int(g*255),int(b*255))
                # im[y][x] = (50,50,50)
    return im
ims = []



# To save the animation, use e.g.
#
# ani.save("movie.mp4")

with open("day 12/input") as f:
    text = f.read().strip()

world = text.split("\n")

height = len(world)
width = len(world[0])


checked = set()
regions = {}
regionnr = 0
regionlabel=world[0][0]
next_region_seeds = [(0,0)]
def get_side_dir(px,py,x,y):
    return abs(y-py),abs(x-px)

while len(checked) < height*width:
    tocheck = []
    localchecked = set()
    next_region_seed = next_region_seeds.pop()
    if next_region_seed in checked:
        continue
    checked.add(next_region_seed)
    localchecked.add(next_region_seed)
    regionnr += 1
    regionlabel = world[next_region_seed[1]][next_region_seed[0]]
    regions[regionnr] = {"a":1,"p":0,"label":regionlabel}
    regionsides = set()
    if regionlabel in "EJ":
        pass
    tocheck.append((next_region_seed[0],next_region_seed[1],next_region_seed[0],next_region_seed[1]+1))
    tocheck.append((next_region_seed[0],next_region_seed[1],next_region_seed[0],next_region_seed[1]-1))
    tocheck.append((next_region_seed[0],next_region_seed[1],next_region_seed[0]+1,next_region_seed[1]))
    tocheck.append((next_region_seed[0],next_region_seed[1],next_region_seed[0]-1,next_region_seed[1]))
    while len(tocheck)>0:
        
        px,py,x,y = tocheck.pop()
        nx,ny = get_side_dir(px,py,x,y)
        if (x,y) in localchecked:
            continue
        if (not (0<=x<width and 0<=y<height)) or world[y][x] != regionlabel:
            a = (px+nx,py+ny,x+nx,y+ny) in regionsides
            b = (px-nx,py-ny,x-nx,y-ny) in regionsides
            if a and b:
                regions[regionnr]["p"] -= 1 # if this edge really is just part of a larger longer edge, that formed from both sides, then it corrects itself
            if a or b:
                pass # dont add an edge if it already exists
            else:
                regions[regionnr]["p"] += 1
            regionsides.add((px,py,x,y)) # extend previous edges
            # regionsides.add((x,y,px,py)) this one is wrong to include 
        if not (0<=x<width and 0<=y<height):
            continue
        if world[y][x] != regionlabel:
            next_region_seeds.append((x,y))
        if world[y][x] == regionlabel:
            checked.add((x,y))
            im = ax.imshow(im_from_checked(checked,localchecked,world,width,height), animated=True)
            ims.append([im])
            localchecked.add((x,y))
            tocheck.append((x,y,x,y+1))
            tocheck.append((x,y,x,y-1))
            tocheck.append((x,y,x+1,y))
            tocheck.append((x,y,x-1,y))
            regions[regionnr]["a"] += 1
        
    # if next_region_seed not in checked:
summ = 0    
for region in regions.values():
    # print(f"A region of {region['label']} plants with price {region['a']} * {region['p']} = {region['a']*region['p']}.")
    summ += region["a"]*region["p"]
print(summ)


ani = animation.ArtistAnimation(fig, ims, interval=8, blit=False,repeat=True)
ani.save("movie.mp4")
plt.show()
# To save the animation, use e.g.
#
pass

