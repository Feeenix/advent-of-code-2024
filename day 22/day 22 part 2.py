"""
BFS: Brute Force Solution.
but optimized
"""

# import numba 
import numpy as np

with open("day 22/input") as f:
    text = f.read().strip()
    

# @numba.njit
def evolve_get_bananas(secret,n):
    prev1v = 0
    prev2v = 0
    prev3v = 0
    prev_this = secret%10
    theset = {}
    for i in range(n):
        secret = ((secret<<6)^secret)&(2**24-1)
        secret = ((secret>>5)^secret)#&(2**24-1)
        secret = ((secret<<11)^secret)&(2**24-1)            
        this = secret%10
        v = this - prev_this
        prev_this = this
        if i >= 3:
            if (v,prev1v,prev2v,prev3v) not in theset:
                theset[(v,prev1v,prev2v,prev3v)] = this
        prev3v = prev2v
        prev2v = prev1v
        prev1v = v           
    return theset


# @numba.njit
def part2(intarray):
    
    sets = {}
    for startsecret in intarray:
        sets[startsecret]= evolve_get_bananas(startsecret,2000)
        # print(startsecret)
    
    unique = set()
    for set_ in sets.values():
        unique.update(set_.keys())
        
    out = 0
    for sequence in unique:
        result = sum([sets[s][sequence] for s in sets if sequence in sets[s] ])

        out = max(out,result)    
    pass
    return out




print(part2(np.array([int(x) for x in text.split("\n")])))
# a = evolve_get_bananas(123,2000)
pass

# total = 0
# for numstr in text.split("\n"):
#     startsecret = int(numstr)
#     total += evolve(startsecret,2000)
# print(total)