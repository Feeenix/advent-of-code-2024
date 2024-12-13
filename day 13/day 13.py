import numpy as np
result = 0
def findAB(ax,ay,bx,by,gx,gy):
    a = np.array([ax,ay])
    b = np.array([bx,by])
    g = np.array([gx,gy])
    
    cursor = np.array([0,0])
    prevcursor = -b
    bs = 0
    while True:
        division = np.divide(g-cursor,a)
        if division[0] == division[1]:
            return division[0], bs
        if np.sign(np.dot(g-prevcursor,(prevcursor[1],prevcursor[0]))) * np.sign(np.dot(g-cursor,(cursor[1],cursor[0]))) <0:
            break
        prevcursor = cursor.copy()
        cursor += b
        bs += 1
    return None
with open("day 13/input") as f:
    while True:
        a = f.readline()
        b = f.readline()
        g = f.readline()
        
        ax,ay = [int(x[2:]) for x in a.split(": ")[1].split(", ")]
        bx,by = [int(x[2:]) for x in b.split(": ")[1].split(", ")]
        gx,gy = [int(x[2:]) for x in g.split(": ")[1].split(", ")]
        r = findAB(ax,ay,bx,by,gx,gy)
        if not r is None:
            result += r[0]*3+r[1]
        e = f.readline()
        if e == "":
            break
print(result)
