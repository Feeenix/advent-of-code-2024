with open("day 17/input") as f:
    text = f.read().strip()
    
reg,program = text.split("\n\n")

# reg = reg.replace("Register ", "")
A,B,C = [int(x.split(": ")[1]) for x in reg.split("\n")]
A = 1523076922204280
instructions = list(map(int,program.split(": ")[1].split(",")))
pc = 0

output = []
while True:
    if pc >= len(instructions):
        break
    # fetch
    opcode = instructions[pc]
    # decode
    literal = instructions[pc+1]
    combo = [0,1,2,3,A,B,C,None][literal]
    pc += 2

    #execute
    if opcode == 0: # adv, divsion, A//(2**combo) → A
        A = A>>combo
    elif opcode == 1: # bxl, bitwise XOR of B and combo to B
        B = B^literal
    elif opcode == 2: # bst, combo % 8  → B
        B = combo%8
    elif opcode == 3: # jnz
        if A != 0:
            pc = literal
    elif opcode == 4: # bxc B XOR C → B
        B = B^C
    elif opcode == 5: # out
        output.append(combo%8)
        
    elif opcode == 6: # bdv, divsion, A//(2**combo) → B
        B = A>>combo
    elif opcode == 7: # cdv, divsion, A//(2**combo) → C
        C = A>>combo


    
    
    #write back
    
    
print(",".join(map(str,output)))


pass
