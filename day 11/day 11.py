with open("day 11/input","r") as f:
    stones = [int(x) for x in f.read().strip().split()]

def update(stone:int) -> list:
    if stone == 0:
        return [1,]
    s = str(stone)
    length = len(s)
    if length%2==0:
        return [int(s[:length//2]),int(s[length//2:])]
    return [stone*2024,]


for i in range(25):    
    new_list = []
    for stone in stones:
        new_list.extend(update(stone))
        
    stones = new_list
    
print(len(stones))
    