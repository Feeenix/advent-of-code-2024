with open("day 17/input") as f:
    text = f.read().strip()

# i think this solution is taylored bespokely to this set of inputs
    
reg,program = text.split("\n\n")

# reg = reg.replace("Register ", "")
# A,B,C = [int(x.split(": ")[1]) for x in reg.split("\n")]

instructions = list(map(int,program.split(": ")[1].split(",")))

# A = 0b000000000000000000000000000000000000000000000000
# known_bits = set() # positions of the known bits

out = []
search_space = [(0,set(),0)]
while search_space:
    # search_space.sort(key=lambda x:x[0],reverse=True)
    A,known_bits,num_index = search_space.pop()
    # print(num_index)
    print(f'{bin(A).replace("0b",""):.>40} {num_index}')
    # out.append(A)
    
    if num_index >= len(instructions)-10:
        # print(bin(A))
        out.append(A)
        # continue
    known_ijk = [num_index*3+i in known_bits for i in range(3)]
    
    known_bits.update([num_index*3+i for i in range(3)])
    
    if not all(known_ijk):
        known_ijk_num = known_ijk[0]+2*known_ijk[1]+4*known_ijk[2] 
        for n in range(2**3): # either 2, 4 or 8
            if n&known_ijk_num : 
                continue
            newA = A|(n<<(3*num_index))
            search_space.append((newA,known_bits.copy(),num_index))
        continue # continue the while loop

    ijk = (A>>(num_index*3))&7
    num = instructions[num_index]
    xyz = (ijk^2)^num^7 # flip 2nd bit
    xyz_in_A = (A>>(num_index*3+(ijk^2)))&7
    known_xyz = [num_index*3+i+(ijk^2) in known_bits for i in range(3)]
    if not any(known_xyz): # everyone is false
        # A|(xyz<<(num_index*3+ijk))
        # known_bits | set([num_index*3+i+ijk for i in range(3)])
        search_space.append((A|(xyz<<(num_index*3+(ijk^2))),known_bits.copy() | set([num_index*3+i+(ijk^2) for i in range(3)]),num_index+1))
        continue
    
    # some are known already
    known_xyz_num = known_xyz[0]+2*known_xyz[1]+4*known_xyz[2]
    
    s = known_xyz_num^xyz_in_A^xyz^7
    if s == 0: # valid
        search_space.append((A|(xyz<<(num_index*3+(ijk^2))),known_bits.copy() | set([num_index*3+i+(ijk^2) for i in range(3)]),num_index+1))
        continue
        
    # otherwise, invalid. skip
    
    
            
        
    
    
    
    
    
    # if all([num_index*3+i in known_bits for i in range(3)])
    
    
    
    
        

# print(out)
print((out))
print(min(out))
print(max(out))

pass
