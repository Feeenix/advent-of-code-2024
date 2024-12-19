with open("day 19/input") as f:
    text = f.read().strip()
    
subpatterns,checkpatterns = text.split("\n\n")

subpatterns = set(subpatterns.split(", "))
largest_subpattern = max(map(len,subpatterns))
checkpatterns = checkpatterns.split("\n")

memoize = {}
def test_if_possible(pattern) -> int: 
    if pattern in memoize:
        return memoize[pattern]
    # if pattern == "":
    #     return 1
    if len(pattern) == 1 and pattern in subpatterns:
        memoize[pattern] = 1
        return 1
    sum_ = 0
    if pattern in subpatterns:
        sum_ += 1
    if pattern == "":
        memoize[pattern] = 0
        return 0
    for i in range(min(largest_subpattern,len(pattern)),0,-1):
        if pattern[:i] in subpatterns:
            test = test_if_possible(pattern[i:])
            if test:
                sum_ +=test
    memoize[pattern] = sum_
    return sum_
            

sum_ = 0
for pattern in checkpatterns:
    test = test_if_possible(pattern)
    # print(test)
    if test:
        sum_+=test

print(sum_)
pass

