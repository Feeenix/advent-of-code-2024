import numpy as np
list1,list2 = zip(*[(int(line.split()[0]),int(line.split()[1])) for line in open('day 1/input').readlines()])
list1 = list(list1)
list2 = list(list2)
list1.sort()
list2.sort()

list2amounts = {i:list2.count(i) for i in list2}

sum_ = 0
for i in list1:
    if i in list2amounts:
        sum_ += i*list2amounts[i]
print(sum_)
