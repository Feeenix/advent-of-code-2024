with open("day 19/testcase") as f:
    text = f.read().strip()
    
subpatterns,checkpatterns = text.split("\n\n")

subpatterns = set(subpatterns.split(", "))
largest_subpattern = max(map(len,subpatterns))
checkpatterns = checkpatterns.split("\n")

def test_if_possible(pattern) -> bool: 
    if pattern in subpatterns:
        return True
    for i in range(largest_subpattern):
        if pattern[:i+1] in subpatterns:
            if test_if_possible(pattern[i+1:]):
                return True
            

sum_ = 0
for pattern in checkpatterns:
    if test_if_possible(pattern):
        sum_+=1

print(sum_)
pass

