import math
import numpy as np
result = 0
def findAB(ax,ay,bx,by,gx,gy):
    a = np.array([ax,ay])
    b = np.array([bx,by])
    g = np.array([gx,gy])
    
    
    
    cursor = np.array([0,0])
    bs = 0

    # finne startposisjonen for å teste mindre

    # x = (g[1]-(b[1]/b[0])*g[0])/((a[1]/a[0])-(b[1]/b[0]))
    # bs = abs(x//b[0])-10
    bs = math.floor((gx/bx -ax*gy/(bx*ay))/(1-ax*by/(bx*ay)))
    cursor = bs*b
    prevcursor = cursor-b

    """


L1 = b*t
L2 = g+a*s
finne t
b*t = g+a*s
bx*t = gx+ax*s
by*t = gy+ay*s => s = (by*t-gy)/ay

t = (gx+ax*s)/bx =gx/bx+ax*s/bx
t = (gx/bx -ax*gy/(bx*ay))/(1-ax*by/(bx*ay))
 
t = (gx+ax*(by*t-gy)/ay)/bx







"""



    
    
    
    for _ in range(2):
        d = np.dot(cursor-g, (-a[1],a[0]))
        dp = np.dot(prevcursor-g, (-a[1],a[0]))
        # division = np.divide(g-cursor,a)
        # if round(division[0],1) == round(division[1],1):
            # return division[0], bs
        if d == 0:
            division = np.divide(g-cursor,a)
            if round(division[0],1) == division[0] or round(division[1],1) == division[1]:
                return division[0], bs # in line and integer amount away
            return None # in line but not integer amount away
        # if np.sign(d)*np.sign(dp) <0:
        if abs(d)>abs(dp) or np.sign(d)*np.sign(dp)==-1: # its moving away from 0
            return None # just passed the line point
        # if np.sign(np.dot(g-prevcursor,(prevcursor[1],prevcursor[0]))) * np.sign(np.dot(g-cursor,(cursor[1],cursor[0]))) <0:
        #     break
        prevcursor = cursor.copy()
        cursor += b
        bs += 1
    # return None
with open("day 13/input") as f:
    while True:
        a = f.readline()
        b = f.readline()
        g = f.readline()
        
        ax,ay = [int(x[2:]) for x in a.split(": ")[1].split(", ")]
        bx,by = [int(x[2:]) for x in b.split(": ")[1].split(", ")]
        gx,gy = [int(x[2:])+10000000000000 for x in g.split(": ")[1].split(", ")]
        r = findAB(ax,ay,bx,by,gx,gy)
        if not r is None:           
            result += int(r[0]*3)+int(r[1])
        e = f.readline()
        if e == "":
            break
print(result)
