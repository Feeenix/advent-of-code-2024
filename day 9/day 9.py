with open("day 9/input") as f:
    text = f.read().strip()

array = list(map(int,list(text)))
r_array = list(reversed(array))
length = len(array)
checksum = 0
# filesystem = []
fileindex = 0
# reversefileindex = 0
i = 0
assert len(array) % 2 == 1
p = -2
reversenum = len(array)//2+1
reverseamount = 0
while True:
    n = array[i]
    blockid = i//2
    for k in range(n):
        if i % 2 == 0:
            # filesystem.append(blockid)
            checksum += fileindex*blockid
        else:
            if reverseamount <= 0:
                p += 2
                reverseamount = r_array[p]
                reversenum -= 1
            reverseamount -= 1
            # filesystem.append(reversenum)
            checksum += fileindex*reversenum

        fileindex += 1

    i += 1
    if i+p+1 >= length:
        break

for a in range(reverseamount):
    # filesystem.append(reversenum)
    checksum += fileindex*reversenum
    fileindex += 1

print(checksum)