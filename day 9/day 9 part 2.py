with open("day 9/input") as f:
    text = f.read().strip()

array = list(map(int,list(text)))
r_array = list(reversed(array))
length = len(array)
checksum = 0
filesystem = []
fileindex = 0
# reversefileindex = 0
i = 0
assert len(array) % 2 == 1
p = -2
reversenum = len(array)//2+1
reverseamount = 0
filled_space = [0]*(len(array)//2)
file_voids = [0]*(len(array)//2+1)
for k in range(len(array)-1 , 0, -2):
    filesize = array[k]
    reversenum-=1
    if reversenum == 2:
        pass
    fileindex = 0
    for j in range(k):
        
        if j%2==1:
            fileindex+=filled_space[j//2]
            voidsize = array[j]
            if voidsize >= filesize:
                for p in range(filesize):
                    checksum += reversenum*(p+fileindex)
                
                file_voids[k//2] = filesize
                array[k] = 0
                array[j] -= filesize
                filled_space[j//2]+=filesize
                break
        fileindex +=array[j]
        if j % 2 == 0:
            fileindex+= file_voids[j//2]
        pass
fileindex = 0
filenum = 0
for k in range(len(array)):
    if k % 2 == 0:
        
        filesize = array[k]
        for p in range(filesize):
            checksum += (k // 2)*(p+fileindex)
    fileindex +=array[k]
    if k % 2 == 1:
        fileindex+=filled_space[k//2]
    else:
        fileindex+= file_voids[k//2]
        pass
        
        

print(checksum)