import numba

with open("day 22/input") as f:
    text = f.read().strip()
    

@numba.njit
def evolve(secret,n):
    for _ in range(n):
        # secret = (((secret&(2**18-1))<<6)^secret)
        # secret = ((secret>>5)^secret)#&(2**24-1)
        # secret = (((secret&(2**13-1))<<11)^secret)
        secret = ((secret<<6)^secret)&(2**24-1)
        secret = ((secret>>5)^secret)#&(2**24-1)
        secret = ((secret<<11)^secret)&(2**24-1)
    return secret

total = 0
for numstr in text.split("\n"):
    startsecret = int(numstr)
    total += evolve(startsecret,2000)
print(total)