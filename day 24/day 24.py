with open("day 24/input") as f:
    text = f.read().strip()
    
    
wires = {}

input_wires,rules = text.split("\n\n")
for line in input_wires.split("\n"):
    key,value = line.split(": ")
    value = (int(value))
    wires[key] = value
    

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

for k in range(len(unique_wires)): #O(n^3)
    for i in range(len(unique_wires)): # bubblesort
        for j in range(i+1,len(unique_wires)):
                
            # if (unique_wires[i] in isbefore and not unique_wires[j] in isbefore[unique_wires[i]]):
            if not unique_wires[j] in isbefore:
                continue
            if unique_wires[i] in isbefore[unique_wires[j]]:
            # if (unique_wires[j], unique_wires[i]) in rule_set:# 
                unique_wires[i],unique_wires[j] = unique_wires[j],unique_wires[i]
            
zs = []

for wire in unique_wires:
    a1,op,a2 = rule_for_wire[wire]
    a1v = wires[a1]
    a2v = wires[a2]
    if op == "AND":
        wires[wire] = a1v&a2v
    elif op == "OR":    
        wires[wire] = a1v|a2v
    elif op == "XOR":    
        wires[wire] = a1v^a2v
    if wire.startswith("z"):
        zs.append((wire,wires[wire]))


zs.sort(key=lambda x: (int(x[0][1:])),reverse=False)

total = 0
for i,(_,z) in enumerate(zs):
    total +=(2**i)*z
print(total)

pass
        
        
        