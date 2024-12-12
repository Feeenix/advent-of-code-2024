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
    
    tocheck.append((next_region_seed[0],next_region_seed[1]+1))
    tocheck.append((next_region_seed[0],next_region_seed[1]-1))
    tocheck.append((next_region_seed[0]+1,next_region_seed[1]))
    tocheck.append((next_region_seed[0]-1,next_region_seed[1]))
    while len(tocheck)>0:
        x,y = tocheck.pop()
        if (x,y) in localchecked:
            continue
        if (not (0<=x<width and 0<=y<height)) or world[y][x] != regionlabel:
            regions[regionnr]["p"] += 1
        if not (0<=x<width and 0<=y<height):
            continue
        if world[y][x] != regionlabel:
            next_region_seeds.append((x,y))
        if world[y][x] == regionlabel:
            checked.add((x,y))
            localchecked.add((x,y))
            tocheck.append((x,y+1))
            tocheck.append((x,y-1))
            tocheck.append((x+1,y))
            tocheck.append((x-1,y))
            regions[regionnr]["a"] += 1
        
    # if next_region_seed not in checked:
summ = 0    
for region in regions.values():
    # print(f"A region of {region['label']} plants with price {region['a']} * {region['p']} = {region['a']*region['p']}.")
    summ += region["a"]*region["p"]
print(summ)
# incomplete_regions = {}

# region_slices = []
# for y in range(height):
#     region_slices.append([])
#     current_region = ""
#     current_region_size = 0
#     current_region_startx = 0
#     for x in range(width):
#         if world[y][x] != current_region:
#             if current_region != "":
#                 region_slices[y].append({"size":current_region_size,"letter":current_region,"startx":current_region_startx,"endx":x,"label":len(incomplete_regions),"perimeter":2})
#                 incomplete_regions[len(incomplete_regions)] = region_slices[y][-1]
#             current_region_size = 1
#             current_region = world[y][x]
#             current_region_startx = x
            
#         else:
#             current_region_size += 1
    
#     region_slices[y].append({"size":current_region_size,"letter":current_region,"startx":current_region_startx,"endx":x+1,"label":len(incomplete_regions),"perimeter":2})
#     incomplete_regions[len(incomplete_regions)] = region_slices[y][-1]
        
# def find_region_at_pos(regions,pos):
#     for i,region in enumerate(regions):
#         if region["startx"]<=pos < region["endx"]:
#             return i,region
#     raise Exception()
# for y in range(height-1):
    
#     for region in region_slices[y]:
#         label = region["label"]
#         if y == 0:
#             incomplete_regions[label]["perimeter"]+=incomplete_regions[label]["size"]
#         for x in range(region["startx"],region["endx"]):
#             index,other_region = find_region_at_pos(region_slices[y+1],x)
#             other_region_label = other_region["label"]
#             if label == other_region_label:
#                 continue
#             incomplete_regions[label]["size"] += incomplete_regions[other_region_label]["size"]
#             incomplete_regions[label]["perimeter"] += incomplete_regions[other_region_label]["perimeter"]
#             incomplete_regions[label]["perimeter"] += abs(incomplete_regions[other_region_label]["startx"]-incomplete_regions[label]["startx"]) + abs(incomplete_regions[other_region_label]["endx"]-incomplete_regions[label]["endx"])
#             other_region["label"] = label
#             other_region["unused"] = True
#             region_slices[y+1][index] = other_region


# for y in range(height):
#     for x in range(width):
#         assert (x,y) in future_region_ids
#         region_id = find_predecessor_region(future_region_ids[(x,y)])
#         if x != width -1:
#             if (x+1,y) not in future_region_ids or future_region_ids[(x+1,y)] == region_id:
#                 if world[y][x+1] == regions[region_id]["letter"]: # cell to the right is the same region as this one
#                     regions[region_id]["area"] += 1
#             elif future_region_ids[(x+1,y)] != region_id and regions[future_region_ids[(x+1,y)]]["letter"] == regions[region_id]["letter"]:
#                 print(f"regions {future_region_ids[(x+1,y)]} and {region_id} are actually the same, even though they have different ids")
#                 deprecated_ids[future_region_ids[(x+1,y)]] = region_id
#                 regions[region_id]["area"] += 1
                
                
pass

