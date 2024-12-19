with open("day 18/input") as f:
    text = f.read().strip()



# for i in range(len(text.split("\n")),0,-1)
walls = {(tuple(map(int,line.split(",")))) for line in  text.split("\n")[0:1024]}
start = (0,0)
end = (70,70)

search_space = [(start,0,70*70+70*70)]
space_gotten_to = {}
def show():
    for y in range(71):
        for x in range(71):
            if (x,y) in walls:
                print("#",end="")
            elif (x,y) in space_gotten_to:
                print("O",end="")
            else:
                print(".",end="")
        print()



def sumv(v1,v2):
    return (v1[0]+v2[0],v1[1]+v2[1])
def dist(v1,v2):
    return ((v1[0]-v2[0])**2+(v1[1]-v2[1])**2)

k = 0
while True:
    search_space.sort(key=lambda x:x[1],reverse=True)
    focus = search_space.pop()
    if k%1000 == 0:
        # show()
        pass
    k+=1
    
    
    if focus[0]==end:
        print(focus[1])
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
                
        search_space.append((sumvector,focus[1]+1,dist(end,sumvector)))
    




pass

