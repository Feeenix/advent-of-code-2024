import sys
sys.setrecursionlimit(12000)
with open("day 11/testcase","r") as f:
    stones = [int(x) for x in f.read().strip().split()]

memoization = {}
def get_length(stone,n)->int:
    if n == 0:
        return 1
    if (stone,n) in memoization:
        return memoization[(stone,n)]
    if stone == 0:
        a = get_length(1,n-1)
        memoization[(stone,n)] = a
        return a
    s = str(stone)
    length = len(s)
    if length%2==0:
        a = get_length(int(s[:length//2]),n-1)+get_length(int(s[length//2:]),n-1)
        memoization[(stone,n)] = a
        return a
    a = get_length(stone*2024,n-1)
    memoization[(stone,n)] = a
    return a
    

total_stones = 0

for stone in stones:
    total_stones += get_length(stone,2166)
print(total_stones)
    