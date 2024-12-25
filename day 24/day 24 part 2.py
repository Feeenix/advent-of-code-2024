with open("day 24/input") as f:
    text = f.read().strip()
    
    
wires = {}
wire_names = {}
names_wire = {}

input_wires,rules = text.split("\n\n")
for line in input_wires.split("\n"):
    key,value = line.split(": ")
    value = (int(value))
    wires[key] = value
    if key[0] in "xy":
        wire_names[key] = key
        names_wire[key] = key
    

rules = rules.split("\n")
rule_for_wire = {}
unique_wires = []
# rule_set = set()
illegal_if_before = {}
isbefore = {}
for rule in rules:
    a1,operation,a2,_,b = rule.split(" ")
    # rule_set.add((a1,b))
    # rule_set.add((a2,b))
    if not a1 in isbefore:
        isbefore[a1] = []
    isbefore[a1].append(b)
    if not a2 in isbefore:
        isbefore[a2] = []
    isbefore[a2].append(b)
    
    
    if not b in illegal_if_before:
        illegal_if_before[b] = []
    illegal_if_before[b].append(a1)
    illegal_if_before[b].append(a2)
    
    
    rule_for_wire[b] = (a1,operation,a2)
    unique_wires.append(b)

for k in range(len(unique_wires)): #O(n^3), continually try to sort until everything has fallen into correct place
    for i in range(len(unique_wires)): # bubblesort
        for j in range(i+1,len(unique_wires)):
                
            # if (unique_wires[i] in isbefore and not unique_wires[j] in isbefore[unique_wires[i]]):
            if not unique_wires[j] in isbefore:
                continue
            if unique_wires[i] in isbefore[unique_wires[j]]:
            # if (unique_wires[j], unique_wires[i]) in rule_set:# 
                unique_wires[i],unique_wires[j] = unique_wires[j],unique_wires[i]

# zs = []
switchings = set()
for wire in unique_wires:
    a1,op,a2 = rule_for_wire[wire]
    
    # if wire in wire_names:
    #     switchings.add(wire_names[wi]re)
    if "knf" in [a1,a2,wire]:
        pass
    bitnum = int(wire_names[a1][1:3])
    bitnum2 = int(wire_names[a2][1:3])
    bitnum,bitnum2 = max(bitnum2,bitnum),min(bitnum2,bitnum)
    inputs = sorted([wire_names[a1],wire_names[a2]])
    bns = str(bitnum).rjust(2,"0")
    bns2 = str(bitnum2).rjust(2,"0")
    nbns = str(bitnum+1).rjust(2,"0")
    pbns = str(bitnum-1).rjust(2,"0")
    if bitnum == 0:
        if inputs == sorted(["x00","y00"]):
            if op == "XOR":
                wire_names[wire] = "z00"
            elif op == "AND":
                wire_names[wire] = "a00"
    else:
        if bitnum2==bitnum and inputs == sorted(["x"+bns,"y"+bns]):
            if op == "XOR":
                wire_names[wire] = "b"+bns
            elif op == "AND":
                wire_names[wire] = "d"+bns
            else:
                print("lost one")
        elif inputs == sorted(["a"+pbns,"b"+bns]):
            if op == "XOR":
                wire_names[wire] = "z"+bns
            elif op == "AND":
                wire_names[wire] = "c"+bns
            else:
                print("lost one")
        elif bitnum2==bitnum and inputs == sorted(["c"+bns,"d"+bns]):
            if op == "OR":
                wire_names[wire] = "a"+bns
            else:
                print("lost one")
        else:
            # print("anomaly at",wire)
            # print(switchings)
            # all gates can be fixed since they all contain 1 correct input and the gate type isnt changed.
            
            if op == "AND" and wire_names[a1][0] == "x":
                switchings.add(wire_names[a2]) # add what it is
                switchings.add("y"+bns)        # add what it should be
                wire_names[wire] = "d"+bns
            elif op == "AND" and wire_names[a2][0] == "x":
                switchings.add(wire_names[a1]) # add what it is
                switchings.add("y"+bns)        # add what it should be
                wire_names[wire] = "d"+bns
            elif op == "AND" and wire_names[a1][0] == "y":
                switchings.add(wire_names[a2]) # simile...
                switchings.add("x"+bns)
                wire_names[wire] = "d"+bns
            elif op == "AND" and wire_names[a2][0] == "y":
                switchings.add(wire_names[a1])
                switchings.add("x"+bns)
                wire_names[wire] = "d"+bns
                    
            elif op == "AND" and wire_names[a1][0] == "b":
                switchings.add(wire_names[a2])
                switchings.add("a"+pbns)
                wire_names[wire] = "c"+bns
            elif op == "AND" and wire_names[a2][0] == "b":
                switchings.add(wire_names[a1])
                switchings.add("a"+pbns)
                wire_names[wire] = "c"+bns
            elif op == "AND" and wire_names[a1][0] == "a":
                switchings.add(wire_names[a2])
                switchings.add("b"+bns)
                wire_names[wire] = "c"+bns
            elif op == "AND" and wire_names[a2][0] == "a":
                switchings.add(wire_names[a1])
                switchings.add("b"+bns)
                wire_names[wire] = "c"+bns
                
            elif op == "OR" and wire_names[a1][0] == "c":
                switchings.add(wire_names[a2])
                switchings.add("d"+bns)
                wire_names[wire] = "a"+bns
            elif op == "OR" and wire_names[a2][0] == "c":
                switchings.add(wire_names[a1])
                switchings.add("d"+bns)
                wire_names[wire] = "a"+bns
            elif op == "OR" and wire_names[a1][0] == "d":
                switchings.add(wire_names[a2])
                switchings.add("c"+bns)
                wire_names[wire] = "a"+bns
            elif op == "OR" and wire_names[a2][0] == "d":
                switchings.add(wire_names[a1])
                switchings.add("c"+bns)
                wire_names[wire] = "a"+bns
                
            elif op == "XOR" and wire_names[a1][0] == "a":
                switchings.add(wire_names[a2])
                switchings.add("b"+bns)
                wire_names[wire] = "z"+bns
            elif op == "XOR" and wire_names[a2][0] == "a":
                switchings.add(wire_names[a1])
                switchings.add("b"+bns)
                wire_names[wire] = "z"+bns
            elif op == "XOR" and wire_names[a1][0] == "b":
                switchings.add(wire_names[a2])
                switchings.add("a"+pbns)
                wire_names[wire] = "z"+bns
            elif op == "XOR" and wire_names[a2][0] == "b":
                switchings.add(wire_names[a1])
                switchings.add("a"+pbns)
                wire_names[wire] = "z"+bns

            elif op == "XOR" and wire_names[a1][0] == "x":
                switchings.add(wire_names[a2])
                switchings.add("y"+bns)
                wire_names[wire] = "b"+bns
            elif op == "XOR" and wire_names[a2][0] == "x":
                switchings.add(wire_names[a1])
                switchings.add("y"+bns)
                wire_names[wire] = "b"+bns
            elif op == "XOR" and wire_names[a1][0] == "y":
                switchings.add(wire_names[a2])
                switchings.add("x"+bns)
                wire_names[wire] = "b"+bns
            elif op == "XOR" and wire_names[a2][0] == "y":
                switchings.add(wire_names[a1])
                switchings.add("x"+bns)
                wire_names[wire] = "b"+bns
            
            else:
            
            
            
                wire_names[wire] = "anomaly"
            
            
            
            
            
            
            
        pass
    



    
    
    
    a1v = wires[a1]
    a2v = wires[a2]
    if op == "AND":
        wires[wire] = a1v&a2v
    elif op == "OR":    
        wires[wire] = a1v|a2v
    elif op == "XOR":    
        wires[wire] = a1v^a2v
    # if wire.startswith("z"):
    #     zs.append((wire,wires[wire]))


# zs.sort(key=lambda x: (int(x[0][1:])),reverse=False)

# # total = 0
# # for i,(_,z) in enumerate(zs):
# #     total +=(2**i)*z
# # # print(total)

names_wire.update({value:key for key,value in wire_names.items()})



switch_wires = [names_wire[label] for label in switchings]
print(",".join(sorted([names_wire[name] for name in set(switchings)])))

pass
        
        
        