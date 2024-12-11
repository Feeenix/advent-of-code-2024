import numpy as np
list1,list2 = zip(*[(int(line.split()[0]),int(line.split()[1])) for line in open('day 1/input').readlines()])
list1 = list(list1)
list2 = list(list2)
list1.sort()
list2.sort()
list1 = np.array(list1)
list2 = np.array(list2)
diff = list2 - list1
abs_diff = np.absolute(diff)
print(sum(abs_diff))
