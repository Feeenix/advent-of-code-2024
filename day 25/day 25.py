with open("day 25/input") as f:
    text = f.read().strip()
    
things = text.split("\n\n")

keys = []
locks = []
for thing in things:
    rows = thing.split("\n")
    horizontal = zip(*rows[1:-1])
    if rows[0] == "#####": # lock
        locks.append(tuple(x.count("#") for x in horizontal))
    if rows[-1] == "#####": # key
        keys.append(tuple(x.count("#") for x in horizontal))
        
    
    
keys_that_fit = {} # (pos,level):set
def find_keys_that_fit(pos,level=0):
    if level == 6:
        return set()
    
    prev_level = find_keys_that_fit(pos,level+1)
    this_level = set()
    for key in keys:
        if key[pos] == 5-level:
            this_level.add(key)
    out = prev_level | this_level
    keys_that_fit[(pos,level)] = out
    return out

for pos in range(5):
    find_keys_that_fit(pos)
    
amount = 0
for lock in locks:
    fit_so_far = keys_that_fit[(0,lock[0])].copy()
    for pos in range(1,5):
        fit_so_far &= (keys_that_fit[(pos,lock[pos])])    
    amount += len(fit_so_far)
    
print(amount)




pass
    
    







    
    
    
    
    
    
    
    
    
    